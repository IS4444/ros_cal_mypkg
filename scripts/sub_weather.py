#!/usr/bin/env python

import subprocess
import rospy
from std_msgs.msg import Int32

def cb(message):
    subprocess.call( "echo 0 > /dev/myled0", shell=True  )
    if message.data == 1:
        rospy.loginfo("Great!!")
        subprocess.call( "echo 1 > /dev/myled0", shell=True  )
    elif message.data == 2:
        rospy.loginfo("Oh...")
        subprocess.call( "echo 2 > /dev/myled0", shell=True  )

if __name__ == "__main__":
    rospy.init_node('answer')
    sub = rospy.Subscriber('cal', Int32, cb)
    rospy.spin()
