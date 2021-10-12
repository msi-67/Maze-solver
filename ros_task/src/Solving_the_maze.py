#!/usr/bin/env python3
import rospy
from math import inf
from sensor_msgs.msg import LaserScan
from std_msgs.msg import Float64
import time

region1 = region2 = region3 = []
min_old = min1 = min2 = min3 = 0

msg1 = LaserScan()


def callback(msg):
    global min_old,region1,region2,region3
    min_old = min(msg.ranges[35:145])  
    region1 = msg.ranges[35:70]
    region2 = msg.ranges [70:110]
    region3 =  msg.ranges [110:145]

def move(a,b,c,d) :
    msg1= Float64()
    msg2= Float64()
    msg3= Float64()
    msg4= Float64()
    msg1.data = a  
    msg2.data = b 
    msg3.data = c 
    msg4.data = d
    pub1.publish(msg1)
    pub2.publish(msg2)
    pub3.publish(msg3)
    pub4.publish(msg4) 
   
def wall():
    global min_old,region1,region2,region3,min1,min2,min3
    x = min_old
    while not rospy.is_shutdown():
        print(x)
        min1 = min(region1)
        min2 = min(region2)
        min3 = min(region3)
        print(min2)
        if(min2 < x + 0.2):
            move(-500,-500,-500,-500)
            print("turning because colliding")
        elif (x - 0.1 <= min1 <= x + 0.1 and min2 > x):
            print("moving")
            move(500,-500,500,-500)
        elif (min1> x + 0.1 and min2 > x) :
            print("turning1")
            move(500,500,500,500)
        elif (min1 < x - 0.5):
            print("turning2")
            move(-500,-500,-500,-500)
        elif (min2 == inf and min3 == inf):
            move(0,0,0,0)
            break
        else:
            print("moving2")
            move(500,-500,500,-500)
      
if __name__ == '__main__':  
 
 try:
    rospy.init_node('wall', anonymous=True)
    pub1 = rospy.Publisher('/joint1_vel_controller/command', Float64, queue_size=10)
    pub2 = rospy.Publisher('/joint2_vel_controller/command', Float64, queue_size=10)
    pub3 = rospy.Publisher('/joint3_vel_controller/command', Float64, queue_size=10)
    pub4 = rospy.Publisher('/joint4_vel_controller/command', Float64, queue_size=10)
    sub = rospy.Subscriber('/laser/scan',LaserScan,callback)
    time.sleep(2)
    wall()
 except rospy.ROSInterruptException:
        pass