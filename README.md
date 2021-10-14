# Maze-solver

## Description 
In this project we are going to simulate a robot using Robot Operating System (ROS) for solving a maze creeated in gazebo enviroment.
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

## Results
FIrst of all, clone this repo in the catkin_ws folder using the terminal.
Change the directory to catkin_ws.
Type  ```catkin_make``` in the terminal, to build the code in catkin workspace.
Type the following command to launch Sahayak with ROS Controls in Gazebo :
``` shell
roslaunch sahayak teleop.launch
```
### Teleoperation
After launching the sahayak bot from previous instructions, run the code in terminal using the following command :
``` shell
rosrun ros_task teleop_sahayak.py
```
![](https://github.com/msi-67/Maze-solver/blob/main/teleop.gif)

### Wall Follower

After launching the sahayak bot from previous instructions, run the code in terminal using the following command :
``` shell
rosrun ros_task Wall_Follower.py
```
![](https://github.com/msi-67/Maze-solver/blob/main/wall_follower.gif)

### Maze - solver

After launching the sahayak bot from previous instructions, run the code in terminal using the following command :
``` shell
rosrun ros_task solving_the_maze.py
```
![](https://github.com/msi-67/Maze-solver/blob/main/maze-solver-1.gif)
![](https://github.com/msi-67/Maze-solver/blob/main/maze-2.gif)

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
