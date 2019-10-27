#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import Float64
import math

def talker():
    
    rospy.init_node('talker', anonymous=True)

    pub1 = rospy.Publisher('/Asimo_E1/joint3_position_controller/command', Float64, queue_size=10)
    
    pub2 = rospy.Publisher('/Asimo_E1/joint4_position_controller/command', Float64, queue_size=10)
    
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        #hello_str = "hello world %s" % rospy.get_time()
        position = 0.0 #math.pi/3
        rospy.loginfo(position)
        pub1.publish(position)
        pub2.publish(position)
        print("pub1:",pub1)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass