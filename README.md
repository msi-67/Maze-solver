# Maze-solver

## Description 
In this project we are goimg to simulate a robot using Robot Operating System (ROS) for solving a maze creeated in gazebo enviroment.
The robot has no prior information regadiing the maze enviroment.
### SAHAYAK BOT was used as a robot in this project. 
#### This project was basically done in 3 steps :
* Teleoperation of Sahayak bot.
* Applying wall following algorithm on a single wall.
* Solving the maze enviroment.

## Tools
* Ubuntu Operating System
* Robot Operating System (ROS) - noetic
* Gazebo

## Python Requirements
``` shell
pip install -r requirement.txt
```
## Required ROS Packages
``` shell
xargs sudo apt install < ros_requirements.txt
```

## Launch Files
`teleop.launch` launch all ROS Controller along with Gazebo.
