#!/usr/bin/env python

""" Example code of how to move a robot around the shape of a square. """

# we always import these
import roslib; roslib.load_manifest('ex_move')
import rospy

# recall: robots generally take base movement commands on a topic 
#  called "cmd_vel" using a message type "geometry_msgs/Twist"
from geometry_msgs.msg import Twist

class square:
    """ This example is in the form of a class. """

    def __init__(self):
        """ This is the constructor of our class. """
        # register this function to be called on shutdown
        rospy.on_shutdown(self.cleanup)

        # publish to cmd_vel
        self.p = rospy.Publisher('cmd_vel', Twist)
        # give our node/publisher a bit of time to connect
        rospy.sleep(1)

        # slow rate, 2 seconds sleep
        r = rospy.Rate(0.5)
        for i in range(4):
            # create a Twist message, fill it in to drive forward
            twist = Twist()
            twist.linear.x = 0.15;
            self.p.publish(twist)
            r.sleep()
            # create a twist message, fill it in to turn
            twist = Twist()
            twist.angular.z = 1.57/2;
            self.p.publish(twist)
            r.sleep()

    def cleanup(self):
        # stop the robot!
        twist = Twist()
        self.p.publish(twist)

if __name__=="__main__":
    rospy.init_node('square')
    square()

