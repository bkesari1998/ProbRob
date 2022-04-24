#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Image

img = Image()
rate = rospy.Rate(1)

# Define a callback for the Image message
def image_callback(img_msg):
    # log some info about the image topic
    rospy.loginfo(img_msg.header)
    img = img_msg

# Initalize a subscriber to the "/camera/rgb/image_raw" topic with the function "image_callback" as a callback
def publish_img():
    rospy.init_node('im_read', anonymous=True)
    sub = rospy.Subscriber('/camera/rgb/image_raw', Image, image_callback)


# Loop to keep the program from shutting down unless ROS is shut down, or CTRL+C is pressed
while not rospy.is_shutdown():
    publish_img()
    rate.sleep()
