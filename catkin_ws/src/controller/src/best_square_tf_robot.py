#!/usr/bin/env python

""" Example code of how to move a robot around the shape of a square, using tf. """
#This is not working on turtlesim. On turtlebot it seemed to work, but further testing is required. The reason it might not be working on turtlesim is due to the transform used, world->turtle1, with might bring trouble. Said transform was adquired from the turtlesim official tutorials, so I thought it should have worked fine, but it didn't. Further review of that transform is required.


# we always import these
import roslib; roslib.load_manifest('ex_move')
import rospy
import tf
import math

# recall: robots generally take base movement commands on a topic 
#  called "cmd_vel" using a message type "geometry_msgs/Twist"
from geometry_msgs.msg import Twist



class square:
    """ This example is in the form of a class. """

    def __init__(self):
        """ This is the constructor of our class. """
	print 'inwut'
        # register this function to be called on shutdown
        rospy.on_shutdown(self.cleanup)

        self.listener = tf.TransformListener()
	print 'k1'

        # publish to cmd_vel
        self.p = rospy.Publisher('cmd_vel', Twist)
        # give our node/publisher a bit of time to connect
        rospy.sleep(1.0)

        twist = Twist()

	#first = True
	for i in range(4):
		print 'hey'
		done = False
		first = 1
		print first

		while not done:
		    # create a Twist message, fill it in to drive forward
		    twist.linear.x = 0.2;
		    twist.angular.z = 0;
		    self.p.publish(twist)
		    rospy.loginfo("moving forward")
		    
		    try:

			((new_x,y,z), rot) = self.listener.lookupTransform('odom', 'base_footprint', rospy.Time(0))

		    except (tf.LookupException, tf.ConnectivityException):
	    		rospy.logerr("AHHHH")

		    #print 'mid!'


		    if first:
			orig_x=new_x
			first=0
			print 'first'		

		    done=bool(abs(new_x-orig_x)>0.8)
	
		    print done
		    print new_x-orig_x
	
		done = False
		first = 1

		while not done:

			twist.angular.z = math.pi/4.0; #turns at pi/4 degrees/sec
			twist.linear.x=0;
			self.p.publish(twist)
			rospy.loginfo("turning")

			try:
		    		((x,y,z), rot) = self.listener.lookupTransform('odom', 'base_footprint', rospy.Time(0))


			except (tf.LookupException, tf.ConnectivityException):
		    		rospy.logerr("AHHHH")

			(phi, psi, theta) = tf.transformations.euler_from_quaternion(rot)

			if first:
				orig_ang=theta
				first=0
			done = bool(abs(theta-orig_ang)>=math.pi/2.0)	

		done = False
		first = 1
		print first

		
            
    
        
    def cleanup(self):
        # stop the robot!
        twist = Twist()
        self.p.publish(twist)

if __name__=="__main__":
    rospy.init_node('square')
    try:
        square()
    except:
        pass
