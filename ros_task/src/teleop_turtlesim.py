#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
import sys, termios, tty, os, time


def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)

    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

def teleop(a,b,c):
    twist = Twist()
    twist.linear.x = a
    twist.linear.y = b
    twist.linear.z = 0
    twist.angular.x = 0
    twist.angular.y = 0
    twist.angular.z = c
    pub.publish(twist)

if __name__ == '__main__':
    rospy.init_node('robot_cleaner', anonymous=True)
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)

    c1 = input("Enter char to move upwards : ")
    c2 = input("Enter char to move downwards : ")
    c3 = input("Enter char to move left : ")
    c4 = input("Enter char to move right : ")
    c5 = input("Enter the key to exit :")
    try:
        while not rospy.is_shutdown(): 
            result= getch()
            if result == c1:
                teleop(2,0,0)
            elif result == c2:
                teleop(-2,0,0)
            elif result == c3:
                teleop(0,0,2)
            elif result == c4:
                teleop(0,0,-2)
            elif result == c5:
                break
    
    except rospy.ROSInterruptException:
        pass






