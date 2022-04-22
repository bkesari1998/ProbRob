#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def publish_cmd():
    print('hello')
    pub = rospy.Publisher('chatter', String, queue_size=10)
    rospy.init_node('cmd_publisher', anonymous=True)
    rate = rospy.Rate(1)
    while not rospy.is_shutdown():
        cmd = raw_input('Enter command: ')
        pub.publish(cmd)
        rate.sleep()

if __name__ == '__main__':
    try:
        publish_cmd()
    except rospy.ROSInterruptException:
        pass

