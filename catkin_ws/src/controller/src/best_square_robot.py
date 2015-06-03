#!/usr/bin/env python
# http://library.isr.ist.utl.pt/docs/roswiki/rospy%282f%29Overview%282f%29Time.html
""" Example code of how to move a robot around the shape of a square. """

import roslib
import rospy
import math
import time
from geometry_msgs.msg import Twist

from kobuki_msgs.msg import Led
from kobuki_msgs.msg import ButtonEvent
from kobuki_msgs.msg import BumperEvent




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
	pub[0].publish(leds[0])

        for i in range(4):

            # create a Twist message, fill it in to drive forward
            twist = Twist()
	    #start = rospy.get_time()
	    start = time.time()
	    while time.time()-start<2:
		print(time.time()-start)
            	twist.linear.x = 0.25; #move 0.5 m/s
		twist.linear.y = 0;
		twist.linear.z = 0;
		twist.angular.x = 0;
		twist.angular.y = 0;
		twist.angular.z = 0;
            	self.p.publish(twist)
		rospy.loginfo("Moving the robot forward.")
            r.sleep()


            twist = Twist()
	    start = time.time()
	    while time.time()-start<2:
		print(time.time())
            	twist.linear.x = 0;
		twist.linear.y = 0;
		twist.linear.z = 0;
		twist.angular.x = 0;
		twist.angular.y = 0;
           	twist.angular.z = math.pi/4.0; #move pi/4 rad/sec
            	self.p.publish(twist)
		rospy.loginfo("Turning the robot")
            r.sleep()
	pub[0].publish(leds[1])

    def cleanup(self):
        # stop the robot!
        twist = Twist()
        self.p.publish(twist)
	pub[0].publish(leds[1])

def ButtonEventCallback(data):
 
    if ( data.button == ButtonEvent.Button0 ) :
        button = "B0"
	if ( data.state == ButtonEvent.RELEASED ) :
		pub[0].publish(leds[1])
		state = "released"
	else:
		pub[0].publish(leds[0])
		square()

    elif ( data.button == ButtonEvent.Button1 ) :
        button = "B1"
	if ( data.state == ButtonEvent.RELEASED ) :
		pub[1].publish(leds[1])
	else:
		pub[1].publish(leds[0])
    else:
        button = "B2"
	if ( data.state == ButtonEvent.RELEASED ) :
		pub[0].publish(leds[1])
		pub[1].publish(leds[1])
	else:
		pub[0].publish(leds[0])
		pub[1].publish(leds[0])


def BumperEventCallback(data):

    if ( data.bumper == BumperEvent.LEFT ) :
        bumper = "Left"
	if ( data.state == BumperEvent.RELEASED ) :
        	pub[0].publish(leds[1])
    	else:
        	pub[0].publish(leds[2])  

    elif ( data.bumper == BumperEvent.CENTER ) :
        bumper = "Center"
	if ( data.state == BumperEvent.RELEASED ) :
        	pub[0].publish(leds[1])
		pub[1].publish(leds[1])
    	else:
        	pub[0].publish(leds[2])
		pub[1].publish(leds[2])

    else:
        bumper = "Right"
	if ( data.state == BumperEvent.RELEASED ) :
        	pub[1].publish(leds[1])
    	else:
        	pub[1].publish(leds[2])



rospy.init_node("controlador")

pub = []
pub.append(rospy.Publisher('/mobile_base/commands/led1',Led))
pub.append(rospy.Publisher('/mobile_base/commands/led2',Led))
leds = []
leds.append(Led())
leds.append(Led())
leds.append(Led())
leds[0].value = Led.GREEN
leds[1].value = Led.BLACK
leds[2].value = Led.RED

rospy.Subscriber("/mobile_base/events/button",ButtonEvent,ButtonEventCallback)
rospy.Subscriber("/mobile_base/events/bumper",BumperEvent,BumperEventCallback)


rospy.spin()

