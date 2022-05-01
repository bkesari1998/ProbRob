#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

def publish_cmd():
    pub = rospy.Publisher('whatever', String, queue_size=10)
    rospy.init_node('cmd_publisher', anonymous=True)
    rate = rospy.Rate(1)
    cmds = ['0', '1', '2', '3']
    while not rospy.is_shutdown():
        cmd = input('Enter command: ')
        if cmd not in cmds:
            continue
        pub.publish(cmd)
        rate.sleep()

if __name__ == '__main__':
    try:
        publish_cmd()
    except rospy.ROSInterruptException:
        pass

