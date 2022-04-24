# CS 152 - HW 5

### Bharat Kesari, Niko Ciminelli, Zach Kratochvil

This repository contains ROS nodes used in the RL navigation task project.

### control_tb.py
This node contains the discrete action space of the robot. The robot can move forward and backward at 0.2 m/s and turn clockwise and counterclockwise at
pi / 6 rad/s. The rate is 1 Hz. This node subscribes to the cmd_pub node and listens for commands. Additionally, the robot reverses for 1 cycle and stops
if it makes contact with an object.

### cmd_pub.py
This node is used to publish commands to the turtlebot. The commands in the action space are f, b, c, and cc, representing the forward and backward movement,
and the clockwise and counter clockwise rotation. The node publishes at a maximum frequency of 1 Hz.

### im_read.py
This node is used to test the turtlebot's camera. It subscribes to the camera and outputs the header of the image it recieves. This node also operates at a 
frequency of 1 Hz.

Additionally, the urdf files for the environment are also in the environent.
