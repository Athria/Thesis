#!/usr/bin/env python
#
## Simple talker demo that published std_msgs/Strings messages
## to the 'chatter' topic

import rospy
from geometry_msgs.msg import Twist
from leap_motion.msg import leapros

def muestra(leap):
    #rospy.loginfo(leap)
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist,queue_size=10)
    twist = Twist()
    
    if leap.normal.z>0:   
	    twist.linear.x = 1; # move forward at 0.1 m/s   
	    rospy.loginfo("Moving the robot forward.")
	    pub.publish(twist)

	    
    elif leap.normal.y<0:
	    rospy.loginfo("Turning the robot left.");
	    twist.angular.z = 0.5
	    pub.publish(twist)
    else:
	    rospy.loginfo(leap);    


def subscribe():
   
    rospy.init_node('control', anonymous=True)
    rospy.Subscriber('/leapmotion/data', leapros, muestra)

    rospy.spin()
    
		  


        
if __name__ == '__main__':
    try:
        subscribe()
    except rospy.ROSInterruptException: pass
