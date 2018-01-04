#!/usr/bin/env python

import rospy
from std_msgs.msg import Int32

def cb(message):
    if message.data == 1:
        rospy.loginfo("Great!!")
    elif message.data == 2:
        rospy.loginfo("Oh...")

if __name__ == "__main__":
    rospy.init_node('answer')
    sub = rospy.Subscriber('cal', Int32, cb)
    rospy.spin()
