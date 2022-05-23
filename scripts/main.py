#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import Float64


def talker():
    
    pub1 = rospy.Publisher('/widowx_arm/joint_2/command', Float64, queue_size=10)
    pub2 = rospy.Publisher('/widowx_arm/joint_3/command', Float64, queue_size=10)
    pub3 = rospy.Publisher('/widowx_arm/joint_4/command', Float64, queue_size=10)
    rospy.init_node('widowx_arm_talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        #hello_str = "hello world %s" % rospy.get_time()
         
        rospy.loginfo(1.0)
        pub1.publish(-1.5)
        pub2.publish(1.5)
        pub3.publish(-1.7)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
