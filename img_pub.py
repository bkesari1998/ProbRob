#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
from rospy_tutorials.msg import Floats
from std_msgs.msg import String
from rospy.numpy_msg import numpy_msg
import numpy as np
import cv2

flag = 0
bridge = CvBridge()

rospy.init_node('image_pub')
rospy.Rate(1)
img_pub = rospy.Publisher('img', numpy_msg(Floats), queue_size=1)

def set_flag(self, data):
    if data.data == str(1):
        flag = 1
    else:
        flag = 0

def image_callback(self, img_msg):
    if flag == 0:
        return
    
    try:
      cv_image = bridge.imgmsg_to_cv2(img_msg, "passthrough")
    except CvBridgeError as e:
      rospy.logerr("CvBridge Error: {0}".format(e))
      return
    
    img = np.array(cv_image)
    img_pub(img)
    flag = 0
    


img_sub = rospy.Subscriber("/camera/rgb/image_raw", Image, image_callback)
flag_sub = rospy.Subscriber('flag', String, set_flag)
img_pub = rospy.Publisher('img', numpy_msg(Floats), queue_size=1)

while not rospy.is_shutdown():
  rospy.spin()