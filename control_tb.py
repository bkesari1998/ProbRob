#!/usr/bin/env python

from math import pi
import rospy
from kobuki_msgs.msg import BumperEvent
from geometry_msgs.msg import Twist
from std_msgs.msg import String


class ControlTB:
    def __init__(self):

        rospy.init_node('ControlTurtleBot', anonymous=False)
        rospy.loginfo("Press CTRL+c to stop TurtleBot")
        rospy.on_shutdown(self.shutdown)

        self.cmd_vel = rospy.Publisher('cmd_vel_mux/input/navi', Twist, queue_size=10)
        self.bumper_sub = rospy.Subscriber('mobile_base/events/bumper', BumperEvent, self.process_bump)
        self.cmd_sub = rospy.Subscriber('chatter', String, self.process_cmd)
        self.rate = rospy.Rate(1)
        self.move_cmd = Twist()
        self.move_cmd.linear.x = 0.2
        self.move_cmd.angular.z = 0

        self.stop = 0

        while not rospy.is_shutdown():
            rospy.spin()

    def process_bump(self, data):
        if (data.state == 1):
            self.stop = 1
            self.move_cmd= Twist()
            self.move_cmd.linear.x = -0.2
            self.cmd_vel.publish(self.move_cmd)
            self.rate.sleep()
            rospy.signal_shutdown('Turtlebot hit something')
    
    def process_cmd(self, data):
        if data.data == 'f':
            self.forward()
        elif data.data == 'b':
            self.backward()
        elif data.data == 'c':
            self.clockwise()
        elif data.data == 'cc':
            self.counter_clockwise()
    
    def shutdown(self):
        self.move_cmd = Twist()
        self.cmd_vel.publish(self.move_cmd)
        self.rate.sleep()
        rospy.loginfo('Stopping turtlebot')
        rospy.sleep(1)

    def forward(self):
        if not self.stop:
            self.move_cmd = Twist()
            self.move_cmd.linear.x = 0.2
            self.cmd_vel.publish(self.move_cmd)
            self.rate.sleep()
    
    def backward(self):
        if not self.stop:
            self.move_cmd = Twist()
            self.move_cmd.linear.x = -0.2
            self.cmd_vel.publish(self.move_cmd)
            self.rate.sleep()

    def clockwise(self):
        if not self.stop:
            self.move_cmd = Twist()
            self.move_cmd.angular.z = -pi / 6
            self.cmd_vel.publish(self.move_cmd)
            self.rate.sleep()

    def counter_clockwise(self):
        if not self.stop:
            self.move_cmd = Twist()
            self.move_cmd.angular.z = pi / 6
            self.cmd_vel.publish(self.move_cmd)
            self.rate.sleep()

    
if __name__ == '__main__':
    try:
        ControlTB()
    except:
        rospy.loginfo("End of the trip for TurtleBot")
    