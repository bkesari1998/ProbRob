#!/usr/bin/env python3

from concurrent.futures import process
import rospy
from std_msgs.msg import String
from rospy.numpy_msg import numpy_msg
from rospy_tutorials.msg import Floats
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
import numpy as np

FORWARD = 0
BACKWARD = 1
LEFT = 2
RIGHT = 3

NUM_STEPS = 10

class Env():
    def __init__(self, ppo_network) -> None:
        super(Env, self).__init__()

        self.action_space = [FORWARD, BACKWARD, LEFT, RIGHT]

        self.steps = 0

        # init node
        rospy.init_node('Env', anonymous=False)

        # command publisher
        self.cmd_pub = rospy.Publisher('command', String, queue_size=1)

        # image array publisher
        self.img_array_sub = rospy.Subscriber('img', numpy_msg(Floats), self.ppo_alg)

        while self.steps < NUM_STEPS:
            rospy.spin()

    def ppo_alg(self, img_msg):

        if self.steps < NUM_STEPS:
            img = img_msg.data

            img_bgr = np.array(cv2.cvtColor(img, cv2.COLOR_RGB2BGR))
            cv2.imshow("Image Window", img_bgr)
            cv2.waitKey(1000)
            cv2.destroyAllWindows()

            # get reward

            # run ppo algorithm

            # publish action
            action = np.random.randint(0, 4).astype(int)[0]
            self.cmd_pub.publish(str(action))

            # increment steps
            self.steps = self.steps + 1


if __name__ == '__main__':
    Env()





        


