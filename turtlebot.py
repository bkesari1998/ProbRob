#!/usr/bin/env python3

import rospy
from kobuki_msgs.msg import BumperEvent
from geometry_msgs.msg import Twist
from std_msgs.msg import String
from math import pi


class TurtleBot:
    def __init__(self) -> None:
        
        # initialize turtlebot node
        rospy.init_node('Turtlebot', anonymous=False)
        rospy.loginfo('Press CTRL-C to stop')
        rospy.on_shutdown(self.shutdown)

        self.cmd_vel = rospy.Publisher('cmd_vel_mux/input/navi', Twist, queue_size=1)
        self.flag_pub = rospy.Publisher('flag', String, queue_size=1)
        self.bumper_sub = rospy.Subscriber('mobile_base/events/bumper', BumperEvent, self.process_bump)
        self.cmd_sub = rospy.Subscriber('command', String, self.process_cmd)

        # run at 10Hz
        self.rate = rospy.Rate(1)

        self.move_cmd = Twist()

        while not rospy.is_shutdown():
            rospy.spin
        
        def process_cmd(self, data):
            if data.data == '0':
                self.forward()
            elif data.data == '1':
                self.backward()
            elif data.data == '2':
                self.clockwise()
            elif data.data == '3':
                self.counter_clockwise()

            flag = "1"
            self.flag_pub.publish(flag)
            
    
        def shutdown(self):
            self.move_cmd = Twist()
            self.cmd_vel.publish(self.move_cmd)
            self.rate.sleep()
            rospy.loginfo('Stopping turtlebot')
            rospy.sleep(1)

        def forward(self):
            if not self.stop:
                self.move_cmd = Twist()
                self.move_cmd.linear.x = 0.1
                self.cmd_vel.publish(self.move_cmd)
                self.rate.sleep()
        
        def backward(self):
            if not self.stop:
                self.move_cmd = Twist()
                self.move_cmd.linear.x = -0.1
                self.cmd_vel.publish(self.move_cmd)
                self.rate.sleep()

        def clockwise(self):
            if not self.stop:
                self.move_cmd = Twist()
                self.move_cmd.angular.z = -pi / 12
                self.cmd_vel.publish(self.move_cmd)
                self.rate.sleep()

        def counter_clockwise(self):
            if not self.stop:
                self.move_cmd = Twist()
                self.move_cmd.angular.z = pi / 12
                self.cmd_vel.publish(self.move_cmd)
                self.rate.sleep()