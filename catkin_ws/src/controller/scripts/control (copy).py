#!/usr/bin/env python
#
## Simple talker demo that published std_msgs/Strings messages
## to the 'chatter' topic

import rospy
from geometry_msgs.msg import Twist

def control():
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist,queue_size=10)
    rospy.init_node('control', anonymous=True)
    twist = Twist()

    r = rospy.Rate(10) # 10hz

    while not rospy.is_shutdown():
            
  	twist.linear.x = 1; # move forward at 0.1 m/s   
   	rospy.loginfo("Moving the robot forward.")
    	pub.publish(twist)
    	rospy.sleep(1)

    	rospy.loginfo("Turning the robot left.");
    	twist = Twist();
    	twist.angular.z = 0.5
    	pub.publish(twist)
	rospy.sleep(1)
    
        r.sleep()


        
if __name__ == '__main__':
    try:
        control()
    except rospy.ROSInterruptException: pass
