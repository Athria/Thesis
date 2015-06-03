#!/usr/bin/env python
# http://library.isr.ist.utl.pt/docs/roswiki/rospy%282f%29Overview%282f%29Time.html
""" Example code of how to move a robot around the shape of a square. """

import roslib
import rospy
import math
import time
from geometry_msgs.msg import Twist


class square:
    """ This example is in the form of a class. """

    def __init__(self):
        """ This is the constructor of our class. """
        # register this function to be called on shutdown
        rospy.on_shutdown(self.cleanup)

        # publish to cmd_vel
        self.p = rospy.Publisher('cmd_vel', Twist)
	#twist = Twist()

        # give our node/publisher a bit of time to connect
        rospy.sleep(1)

        # slow rate, 2 seconds sleep
        r = rospy.Rate(0.5)


        for i in range(4):

            # create a Twist message, fill it in to drive forward
            twist = Twist()
	    start = rospy.get_time()
	    print(rospy.get_time())
	    while rospy.get_time()-start<4:
            	twist.linear.x = 0.25; #move 0.25 m/s
		twist.linear.y = 0;
		twist.linear.z = 0;
		twist.angular.x = 0;
		twist.angular.y = 0;
		twist.angular.z = 0;
            	self.p.publish(twist)
		rospy.loginfo("Moving the robot forward.")
            r.sleep()


            twist = Twist()
	    start = rospy.get_time()
	    print(rospy.get_time())
	    while rospy.get_time()-start<2:
            	twist.linear.x = 0;
		twist.linear.y = 0;
		twist.linear.z = 0;
		twist.angular.x = 0;
		twist.angular.y = 0;
           	twist.angular.z = math.pi/4.0; #move pi/4 rad/sec
            	self.p.publish(twist)
		rospy.loginfo("Turning the robot")
            r.sleep()

    def cleanup(self):
        # stop the robot!
        twist = Twist()
        self.p.publish(twist)

if __name__=="__main__":
    rospy.init_node('control', anonymous=True)
    square()
