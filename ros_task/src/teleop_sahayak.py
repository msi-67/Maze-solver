#!/usr/bin/env python3

import rospy 
from std_msgs.msg import Float64
import sys, termios, tty, os, time

def  getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)

    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

def move(a,b,c,d):
    msg1 = Float64()
    msg2 = Float64()
    msg3 = Float64()
    msg4 = Float64()
    msg1.data = a
    msg2.data = b
    msg3.data = c
    msg4.data = d
    pub.publish(msg1)
    pub1.publish(msg2)
    pub2.publish(msg3)
    pub3.publish(msg4)

if __name__ == '__main__' :
    rospy.init_node('Sahayak_teleop', anonymous=True)
    pub = rospy.Publisher('/joint1_vel_controller/command', Float64, queue_size=10)
    pub1 = rospy.Publisher('/joint2_vel_controller/command', Float64, queue_size=10)
    pub2 = rospy.Publisher('/joint3_vel_controller/command', Float64 ,queue_size=10)
    pub3 = rospy.Publisher('/joint4_vel_controller/command', Float64 ,queue_size=10)
    c1 = input("Enter char to move pos x direction: ")
    c2 = input("Enter char to move neg y direction : ")
    c3 = input("Enter char to rotate in +ve direction : ")
    c4 = input("Enter char to rotate in -ve direction : ")
    c5 = input("Enter the key to exit :")
    
    try:
        while not rospy.is_shutdown():
            result = getch()
            if result == c1 :
                move(16,-16,16,-16)
            elif result == c2:
                move(-16,16,-16,16)
            elif result == c3:
                move(16,16,16,16)
            elif result == c4:
                move(-16,-16,-16,-16)
            elif result == c5:
                move(0,0,0,0)
                break
    
    except rospy.ROSInterruptException:
        pass

            
            




    