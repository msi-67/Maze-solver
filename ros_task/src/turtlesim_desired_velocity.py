#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
import math

def move():
    rospy.init_node('robot_cleaner', anonymous=True)
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    vel_msg = Twist()

    print("Let's move your robot")
    speed1 = int(input("Input the x velocity : "))
    speed2 = int(input("Enter the y velocity : "))
    speed3 = int(input("Enter the z velocity : "))
    angspeed1 = int(input("Enter the x angular velocity : "))
    angspeed2 = int(input("Enter the y angular velocity : "))
    angspeed3 = int(input("Enter the z angular velocity : "))
    distance = math.sqrt(speed1**2 + speed2**2 + speed3**2)
 
    
    vel_msg.linear.x = speed1
    vel_msg.linear.y = speed2
    vel_msg.linear.z = speed3
    vel_msg.angular.x = angspeed1
    vel_msg.angular.y = angspeed2
    vel_msg.angular.z = angspeed3

    while not rospy.is_shutdown():

        t0 = rospy.Time.now().to_sec()
        current_distance = 0
        while(current_distance < distance):
            velocity_publisher.publish(vel_msg)
            t1=rospy.Time.now().to_sec()
            if speed1 != 0 :
                current_distance = abs(speed1)*(t1-t0)
            elif speed2 != 0 :
                current_distance = abs(speed2)*(t1-t0)
            elif speed3 != 0 :
                current_distance = abs(speed3)*(t1-t0)
        vel_msg.linear.x = 0
        vel_msg.linear.y = 0
        vel_msg.linear.z = 0
        vel_msg.angular.x = 0
        vel_msg.angular.y = 0
        vel_msg.angular.z = 0
        velocity_publisher.publish(vel_msg)

if __name__ == '__main__':
    try:
        #Testing our function
        move()
    except rospy.ROSInterruptException: pass