#!/usr/bin/env python
#
## Simple talker demo that published std_msgs/Strings messages
## to the 'chatter' topic

import roslib
import rospy
from geometry_msgs.msg import Twist

pub = rospy.Publisher('/turtle1/cmd_vel', Twist,queue_size=10)
twist = Twist()
rospy.init_node('control', anonymous=True)
#r = rospy.Rate(2) # 10hz
while not rospy.is_shutdown():


	for i in range(30):
		twist.linear.x = 0.75; # move forward at 0.1 m/s 
		twist.angular.z = 0;  
		rospy.loginfo("Moving the robot forward.")
		pub.publish(twist)
   		rospy.sleep(0.1)

	for i in range(30):
		twist.angular.z = 0.523; # move forward at 0.1 m/s   
		twist.linear.x = 0;
		rospy.loginfo("Turn 1")
		pub.publish(twist)
	   	rospy.sleep(0.1)

	for i in range(30):
		twist.linear.x = 0.75; # move forward at 0.1 m/s 
		twist.angular.z = 0;     
		rospy.loginfo("Moving the robot forward.")
		pub.publish(twist)
	   	rospy.sleep(0.1)

	for i in range(30):
		twist.angular.z = 0.523; # move forward at 0.1 m/s 
		twist.linear.x = 0;  
		rospy.loginfo("Turn 2")
		pub.publish(twist)
	   	rospy.sleep(0.1)
