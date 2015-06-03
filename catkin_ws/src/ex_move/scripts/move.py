#!/usr/bin/env python

""" Example code of how to move a robot back and forth. """

# we always import these
import roslib; roslib.load_manifest('ex_move')
import rospy

# recall: robots generally take base movement commands on a topic 
#  called "cmd_vel" using a message type "geometry_msgs/Twist"
from geometry_msgs.msg import Twist

x_speed = 0.2  # 0.1 m/s
r_angle = 0.0  # 0.1 rad/s

# a nasty global variable
p = None

def cleanup():
    """ You should put comments like this inside each function. 
        This function is called when the node shuts down -- it stops the robot. """
    global p
    p.publish(Twist())


# this quick check means that the following code runs ONLY if this is the 
# main file -- if we "import move" in another file, this code will not execute.
if __name__=="__main__":

    # first thing, init a node!
    rospy.init_node('move')

    # setup to call this function on node exit
    rospy.on_shutdown(cleanup)

    # publish to cmd_vel
    p = rospy.Publisher('cmd_vel', Twist)

    r = rospy.Rate(10)
    # counter
    c = 0
    while not rospy.is_shutdown():
        # create a twist message, fill in the details
        twist = Twist()
        twist.linear.x = x_speed; twist.linear.y = 0; twist.linear.z = 0;            
        twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = r_angle;

        # publish the message
        p.publish(twist)

        # robot drives back and forth, about 4 seconds in each direction
        c = c + 1
        if c > 40:
            x_speed = -0.2
        if c > 80:
            c = 0
            x_speed = 0.2

        # sleep for 1/10 of a second
        r.sleep()


