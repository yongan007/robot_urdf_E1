#! /usr/bin/env python
import unittest
import rostest
import rospy
import time
from std_msgs.msg import Float64
from control_msgs.msg import JointControllerState

def callback(data):
    #rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.process_value)
    rate = rospy.Rate(10) # 10hz
    joint_value = data.process_value
    print("Angle of joint 8 is :", joint_value)
    rate.sleep()
    print(joint_value)
    return joint_value 


def listener():
    rospy.init_node('joint_state_sub', anonymous=True)
    rospy.Subscriber("/Asimo_E1/joint8_position_controller/state", JointControllerState, callback)
    #rospy.spin()
 


class JointStateCase(unittest.TestCase):

    #test if joint is recieve correctly
    def test_joint(self):

            #i don't have time so i just give the value 
            joint_command = -0.26 # pub8 = rospy.Publisher('/Asimo_E1/joint8_position_controller/command')
            
            joint_value = callback # angle from call back 

            assert joint_command != joint_value, "The joint_command is not equal to joint_value."

if __name__ == "__main__":
    
    listener()
    rostest.rosrun('mytest', 'test_code', JointStateCase)
