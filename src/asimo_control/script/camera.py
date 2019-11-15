#!/usr/bin/env python


#This code is modified from : #https://gist.github.com/rethink-imcmahon/77a1a4d5506258f3dc1f

# rospy for the subscriber
import rospy
# ROS Image message
from sensor_msgs.msg import Image
# ROS Image message -> OpenCV2 image converter
from cv_bridge import CvBridge, CvBridgeError
# OpenCV2 for saving an image
import cv2
import time

# Instantiate CvBridge
bridge = CvBridge()

t0 =int(time.time())

def image_callback(msg):
    print("Received an image!")
    try:
        # Convert your ROS Image message to OpenCV2
        cv2_img = bridge.imgmsg_to_cv2(msg, "bgr8")
    except CvBridgeError as e:
        print(e)
    else:
        # Save your OpenCV2 image as a jpeg 
        # if t < 0:
        t = str(int(time.time())-t0+1)
        #print(t)
        # else:
        if int(t) <= 10:
            cv2.imwrite('/home/yong_ros/example_ws/src/asimo_e1_description/Photos/camera_image'+t+'.jpeg', cv2_img)
        else:
            pass
        
        # else:
        #     cv2.imwrite('camera_image.jpeg', cv2_img)

def main():
    
    rospy.init_node('image_listener')
    # Define your image topic
    image_topic = "/asimo/camera1/image_raw"
    # Set up your subscriber and define its callback
    rospy.Subscriber(image_topic, Image, image_callback)
    # Spin until ctrl + c
    rospy.spin()

if __name__ == '__main__':
    main()
