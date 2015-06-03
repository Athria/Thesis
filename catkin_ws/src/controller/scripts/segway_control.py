#!/usr/bin/env python
#
## Simple talker demo that published std_msgs/Strings messages
## to the 'chatter' topic

import rospy
from geometry_msgs.msg import Twist
from leap_motion.msg import leapros


def control(leap):

    pub = rospy.Publisher('/segway_rmp_node/cmd_vel', Twist,queue_size=10)
    twist = Twist()


    
    if leap.palmpos.y<200: 
	
	
	if leap.palmpos.z<-30 and abs(leap.palmpos.x)<30:
	
	    twist.linear.x = 0.1   
	    rospy.loginfo("Moving the robot forward.")
	    pub.publish(twist)
	    #r.sleep()	
	    
	elif leap.palmpos.z>30 and abs(leap.palmpos.x)<30:
	
	    twist.linear.x = -0.1    
	    rospy.loginfo("Moving the robot backwards.")
	    pub.publish(twist)
	    
	elif leap.palmpos.x>30 and abs(leap.palmpos.z)<30:
	
	    rospy.loginfo("Turning the robot right.");
	    twist.angular.z = -0.05
	    pub.publish(twist)
	    
	    
	elif leap.palmpos.x<-30 and abs(leap.palmpos.z)<30:
    
	    twist.angular.z = 0.05    
	    rospy.loginfo("Turning the robot left.")
	    pub.publish(twist)


	else:
		rospy.loginfo("Don't move");   
	
	    
    else:
	
	rospy.loginfo("Hand away from controller");
    #leapold=leap    
	    
	    
	    


def Leapdata():
   
    rospy.init_node('Leap_control', anonymous=True)
    
    rospy.Subscriber('/leapmotion/data', leapros, control)

    
    rospy.spin()
    
		  


        
if __name__ == '__main__':
    try:
        Leapdata()
    except rospy.ROSInterruptException: pass