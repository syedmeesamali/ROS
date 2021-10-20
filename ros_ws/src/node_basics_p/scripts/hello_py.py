#!/usr/bin/python3

import rospy

rospy.init_node("hello_log_py")
loop_hz = rospy.Rate(10)
while not rospy.is_shutdown():
	rospy.loginfo("Hello from python node!")
	loop_hz.sleep()
