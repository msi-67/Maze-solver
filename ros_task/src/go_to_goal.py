#! /usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import math

def pose_callback(msg):
    pose_msg.x = msg.x
    pose_msg.y = msg.y
    pose_msg.theta = msg.theta
    pose_msg.linear_velocity = msg.linear_velocity
    pose_msg.angular_velocity = msg.angular_velocity

def distance(x1,y1,x2,y2):
    dist = abs(math.sqrt(((x1-x2)**2)+((y1-y2)**2)))
    return dist

def angvel(x1,y1,x2,y2):
    ang_vel = math.atan2(y1-y2,x1-x2)
    return ang_vel

def move():
    rospy.init_node('onemotion_try', anonymous=True)
    velocity_publisher=rospy.Publisher('/turtle1/cmd_vel',Twist,queue_size=10)
    pose_subscriber=rospy.Subscriber('/turtle1/pose',Pose,pose_callback)
    vel_msg = Twist()
    global pose_msg
    pose_msg=Pose()
    goal_x=int(input("enter x direction:"))
    goal_y=int(input("enter y direction"))

    while (lin_vel < 0.01):
        lin_vel = distance(goal_x,goal_y,pose_msg.x,pose_msg.y)
        angle_vel = angvel(goal_x,goal_y,pose_msg.x,pose_msg.y)
        vel_msg.linear.x= 0.5 * (lin_vel)
        vel_msg.linear.y = 0
        vel_msg.linear.z= 0
        vel_msg.angular.x = 0
        vel_msg.angular.y = 0
        vel_msg.angular.z = 3 * (angle_vel-pose_msg.theta)
        velocity_publisher.publish(vel_msg)
        print(pose_msg)


if __name__ == '__main__':
    try:
        move()
    except rospy.ROSInterruptException: pass
