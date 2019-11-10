#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import Float64
import math

def talker():
    
    rospy.init_node('talker', anonymous=True)

    pub3 = rospy.Publisher('/Asimo_E1/joint3_position_controller/command', Float64, queue_size=10)
    pub4 = rospy.Publisher('/Asimo_E1/joint4_position_controller/command', Float64, queue_size=10)
    
    pub5 = rospy.Publisher('/Asimo_E1/joint5_position_controller/command', Float64, queue_size=10)
    pub6 = rospy.Publisher('/Asimo_E1/joint6_position_controller/command', Float64, queue_size=10)
    
    pub7 = rospy.Publisher('/Asimo_E1/joint8_position_controller/command', Float64, queue_size=10)
    pub8 = rospy.Publisher('/Asimo_E1/joint9_position_controller/command', Float64, queue_size=10)
    
    i=0
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
     
        position = -math.pi/6+math.pi/12
        position1 = math.pi/6
        position2 = -math.pi/12

        rospy.loginfo(position)
        
        pub3.publish(position)
        pub4.publish(position)
        rate.sleep()
        pub5.publish(position1+i)
        pub6.publish(position1+i)

        pub7.publish(position2)
        pub8.publish(position2)

        i=+1
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass