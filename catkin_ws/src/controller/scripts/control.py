#!/usr/bin/env python
#
## Simple talker demo that published std_msgs/Strings messages
## to the 'chatter' topic

import rospy
from geometry_msgs.msg import Twist
from leap_motion.msg import leapros


def control(leap):
    #rospy.loginfo(leap)
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist,queue_size=10)
    twist = Twist()
    #r = rospy.Rate(100) # 10hz

    
    if leap.palmpos.y<200: 
	
	
	if leap.palmpos.z<-30 and abs(leap.palmpos.x)<30:
	
	    twist.linear.x = 0.05 # move forward at 0.05 m/s   
	    rospy.loginfo("Moving the robot forward.")
	    pub.publish(twist)
	    #r.sleep()	
	    
	elif leap.palmpos.z>30 and abs(leap.palmpos.x)<30:
	
	    twist.linear.x = -0.05 # move forward at 0.05 m/s   
	    rospy.loginfo("Moving the robot backwards.")
	    pub.publish(twist)
	    
	elif leap.palmpos.x>30 and abs(leap.palmpos.z)<30:
	
	    rospy.loginfo("Turning the robot right.");
	    twist.angular.z = -0.05
	    pub.publish(twist)
	    
	    
	elif leap.palmpos.x<-30 and abs(leap.palmpos.z)<30:
    
	    twist.linear.z = 0.05 # move forward at 0.05 m/s   
	    rospy.loginfo("Turning the robot left.")
	    pub.publish(twist)
	    #r.sleep()

	else:
		rospy.loginfo("Don't move");   
		#r.sleep()	
	    
    	    
    #leapold=leap    
	    
	    
	    


def Leapdata():
   
    rospy.init_node('Leap_control', anonymous=True)
    
    rospy.Subscriber('/leapmotion/data', leapros, control)

    
    rospy.spin()
    
		  


        
if __name__ == '__main__':
    try:
        Leapdata()
    except rospy.ROSInterruptException: pass