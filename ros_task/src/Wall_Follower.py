#!/usr/bin/env python3
from math import inf
from logging import info
import rospy
from std_msgs.msg import Float64
from sensor_msgs.msg import LaserScan
import time

def move(a,b,c,d):
    msg1 = Float64()
    msg2 = Float64()
    msg3 = Float64()
    msg4 = Float64()
    msg1.data = a
    msg2.data = b
    msg3.data = c
    msg4.data = d
    j1.publish(msg1)
    j2.publish(msg2)
    j3.publish(msg3)
    j4.publish(msg4)


data = LaserScan()
a=b=c=0

def update(data):
    global a,b,c,d
    p = data
    a = min(p.ranges)
    b = p.ranges
    c = b.index(a)
    
        
def goal():
    global a,b,c,d
    print(a)
    while not rospy.is_shutdown():
        mini = b[c]
        print(mini)
        while(True):
            d = b[0:50]
            e = b[120:179]
            count2 = d.count(inf)
            count3 = e.count(inf)
            print(count2)
            print (count3)
            print(c)
            count1 = 0
            if(mini - 0.2 <= b[c] <= mini+0.5):
                print("moving")
                move(5,-5,5,-5)
            elif(b[c] > mini + 0.1 and (c>150 or c<30)):
                print("greater distance turning.")
                move(-5,-5,-5,-5)

            elif(b[c] < mini - 0.2 and (c<170 and c>10)):
                print("TUrning other side.")
                move(5,5,5,5)
            else:
                print("moving 2")
                move(5,-5,5,-5)
            print(mini - 0.3)
            print(mini)
            #if(count2 == 0):
             #   print("no infinite")
              #  move(5,-5,5,-5)
            #elif(count3 == 0):
               # print("no infinite")
                #move(5,-5,5,-5)
            if((c > 120 or c == inf) and count3 > 40):
                print("infinite coming. turning")
                move(-5,-5,-5,-5)
            elif((c < 50 or c == inf) and count2 > 40):
                move(-5,-5,-5,-5)

                


if __name__ == "__main__":
    try:
        rospy.init_node("kaam", anonymous=True)
        global j1,j2,j3,j4
        j1 = rospy.Publisher('joint1_vel_controller/command',Float64,queue_size=10)
        j2 = rospy.Publisher('joint2_vel_controller/command',Float64,queue_size=10)
        j3 = rospy.Publisher('joint3_vel_controller/command',Float64,queue_size=10)
        j4 = rospy.Publisher('joint4_vel_controller/command',Float64,queue_size=10)
        pos = rospy.Subscriber('/laser/scan',LaserScan,update)
        time.sleep(2)
        p = LaserScan()
        goal()
        

    except rospy.ROSInterruptException:
        pass
