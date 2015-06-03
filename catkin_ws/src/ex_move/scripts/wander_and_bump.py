#!/usr/bin/env python

""" Example of using SMACH to wander and bump. """

# we always import these
import roslib; roslib.load_manifest('ex_move')
import rospy

import smach, smach_ros
from smach import State
from smach_ros import *

from irobot_create_2_1.msg import SensorPacket
from irobot_create_2_1.srv import *

class BumpCheckState(smach.State):
    """ This class is a state which checks the status of the bumpers. """
    def __init__(self):
        smach.State.__init__(self, outcomes=['clear','left_collision','right_collision'])
        self.left_bump = False
        self.right_bump = False
        rospy.Subscriber("sensorPacket",SensorPacket,self.sensorCb)
    
    def execute(self, userdata):
        if self.left_bump:
            return 'left_collision'
        elif self.right_bump:
            return 'right_collision'
        else:
            return 'clear'

    def sensorCb(self, msg):
        """ Callback to store bumper state as it arrives. """
        self.left_bump = msg.bumpLeft
        self.right_bump = msg.bumpRight

class WaitState(smach.State):
    """ This class is a state that just waits a designated amount of time before continuing. """
    def __init__(self):
        smach.State.__init__(self, outcomes=['done'])
    def execute(self, userdata):
        rospy.sleep(0.1)
        return 'done'

def main():
    rospy.init_node("wander_and_bump")
    
    rospy.wait_for_service('tank')
    tank = rospy.ServiceProxy('tank',Tank)    

    # Create a SMACH state machine
    sm = smach.StateMachine(outcomes=['succeeded','preempted','aborted'])

    # Open the container
    with sm:
        smach.StateMachine.add('BUMP', BumpCheckState(), 
                               transitions={'clear':'DRIVE',
                                            'left_collision':'TURN_RIGHT',
                                            'right_collision':'TURN_LEFT'})
        smach.StateMachine.add('DRIVE', ServiceState('tank', Tank, request = TankRequest(0,50,50)),
                               transitions={'succeeded':'WAIT'})
        smach.StateMachine.add('TURN_LEFT', ServiceState('tank', Tank, request = TankRequest(0,-100,100)),
                               transitions={'succeeded':'WAIT'})
        smach.StateMachine.add('TURN_RIGHT', ServiceState('tank', Tank, request = TankRequest(0,100,-100)),
                               transitions={'succeeded':'WAIT'})
        smach.StateMachine.add('WAIT', WaitState(), 
                               transitions={'done':'BUMP'})

    # start viewing
    sis = smach_ros.IntrospectionServer('wab_debug',sm,'/SM_ROOT')
    sis.start()

    # wait for ctrl-c
    outcome = sm.execute()
    rospy.spin()
    sis.stop()
    # stop the robot
    tank(0,0,0)

if __name__=="__main__":
    main()

