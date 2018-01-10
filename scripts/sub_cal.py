#!/usr/bin/env python

import wiringpi as w
import rospy
from std_msgs.msg import Int32

led_pin = 23
w.wiringPiSetup()
w.pinMode( led_pin, 1 )

def cb(message):
    if message.data == 1:
        rospy.loginfo("Great!!")
        w.digitalWrite( led_pin, 1 )
    elif message.data == 2:
        rospy.loginfo("Oh...")
        w.digitalWrite( led_pin, 0 )

if __name__ == "__main__":
    rospy.init_node('answer')
    sub = rospy.Subscriber('cal', Int32, cb)
    rospy.spin()
