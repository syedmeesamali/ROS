#!/usr/bin/python3
import rospy
from std_msgs.msg import String

def talker():
	pub = rospy.Publisher('hello_pub', String, queue_size = 10)
	rospy.init_node('hello_world_pub', anonymous = True)
	r = rospy.Rate(10)			#10 Hertz
	while not rospy.is_shutdown():
		str = "hello world %s"%rospy.get_time()
		rospy.loginfo(str)
		pub.publish(str)
		r.sleep()

if __name__ == '__main__':
	try:
		talker()
	except rospy.ROSInterruptException: pass
		
	
