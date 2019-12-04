#!/usr/bin/env python
import rospy
from std_msgs.msg import Float64
from control_msgs.msg import JointControllerState

def callback(data):
    #rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.process_value)
    rate = rospy.Rate(10) # 10hz

    joint_value = data.process_value

    print("Angle of joint 8 is :", joint_value)
    rate.sleep()

    return joint_value 

def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('joint_state_sub', anonymous=True)
    rospy.Subscriber("/Asimo_E1/joint8_position_controller/state", JointControllerState, callback)

    # spin() simply keeps python from exiting until this node is stopped
    
    rospy.spin()

if __name__ == '__main__':
    listener()
 