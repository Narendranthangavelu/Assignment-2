#!/usr/bin/env python
import rospy
import threading
from geometry_msgs.msg import Twist

# get linear velocity and radius of circle
def get_values():
    linear = float(input("\n \nEnter the linear_velocity(0.5 to 3 units) = "))
    if linear < 0.5 or linear > 3.0 :
        linear = 1.0
	rospy.logwarn("Enter values in range")
    radius = float(input("Enter the radius(2 to 5 units) = "))
    if radius < 2.0 or radius > 5.0 :
        radius =2.0
	rospy.logwarn("Enter values in range")
    angular = linear/radius
    return linear,angular

# get keyboard interrupt to stop the circular motion
def quit():
    global key_press
    i = raw_input("\n \nPress enter to stop\n \n")
    key_press = False


def publish():
    global key_press
    pub = rospy.Publisher('husky_velocity_controller/cmd_vel', Twist, queue_size=100)
    rospy.init_node('circle_creater', anonymous=True)
    while not rospy.is_shutdown():
	key_press = True
	linear = 0.0
	angular = 0.0
	radius = 0.0

	#get linear and angular velocity
	try:
		linear, angular = get_values()
	except:
		rospy.logerr("\nEnter only numbers\n")
		continue
	# thread to stop the loop
	a = threading.Thread(target = quit)
	a.daemon = True
	print("Linear Vel = {} \nAngular_Vel = {}".format(linear,angular))

	#start the thread
	a.start()
	
	#publishing the twist values
	rate = rospy.Rate(5) # cmd_vel time out is .25 seconds.
	while key_press and not rospy.is_shutdown():
		command = Twist()
		command.linear.x = linear
		command.angular.z = angular
		pub.publish(command)
		rate.sleep()


if __name__ == '__main__':
    publish()
