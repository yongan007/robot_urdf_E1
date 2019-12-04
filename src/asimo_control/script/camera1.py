#!/usr/bin/python2.7
# license removed for brevity
import os
import rospy
from std_msgs.msg import Float64
from sensor_msgs.msg import Image
import time
# ROS Image message -> OpenCV2 image converter
from cv_bridge import CvBridge, CvBridgeError
# OpenCV2 for saving an image
import cv2

path = os.path.dirname(os.path.realpath(__file__))

# Instantiate CvBridge
bridge = CvBridge()

class ImageSaver:

	def __init__(self):
		self.number = 0
		self.ImagePath = path

	def image_callback(self, msg):
		rate = rospy.Rate(30) # 30hz
		try:
			# Convert ROS Image message to OpenCV2
			cv2_img = bridge.imgmsg_to_cv2(msg, "bgr8")
		except CvBridgeError as e:
			print(e)
		else:
			self.number += 1
			print("Image"+str(self.number)+" saved")
			filename = path+'/Images/' +'camera_image'+str(self.number)+'.jpeg'
			cv2.imwrite(filename, cv2_img)
		rate.sleep()

	def move_joint(joint_num, min, max, pub):
		pos = random.uniform(min,max)
		if not rospy.is_shutdown():
			hello_str = "Joint world! %s" % rospy.get_time()
			position = pos
			rospy.loginfo(position)
			pub.publish(position)
			rate.sleep()

	def main(self):
		time.sleep(10)
		rospy.init_node('camera_image_saver')
		# Image topic
		image_topic = "/asimo/camera1/image_raw"
		# Set up your subscriber and define its callback
		rospy.Subscriber(image_topic, Image, self.image_callback)
		# Spin until ctrl + c
		rospy.spin()

if __name__ == '__main__':
	try:
	
		saver = ImageSaver()
		saver.main()
		rospy.spin()
	except rospy.ROSInterruptException:
		pass


