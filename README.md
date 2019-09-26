## URDF model of Robot Asimo E1

Package Name: description 
Launch folder: urdf.launch, gazebo.launch, xacro.launch 
Urdf folder: robot.urdf, gazebo.urdf, robot_E1.xacro

## Quick Start
To run robot in rviz with xacro: 
	
	roslaunch description xacro.launch 

To run robot in rviz with urdf: 
	
	roslaunch description urdf.launch

To run robot in Gazebo: 
	
	roslaunch description gazebo.launch


##Erro Issue 

In case the robot does not show properly, it maybe becuase of your langeuage in your system is not en_US.UTF-8 in default. to solve this please type:  echo 'export LC_NUMERIC="en_US.UTF-8"' >>~/.bashrc



Created with ROS melodic 
Student: Voeurn Yong Ann, 
Innopolis University
Master of Robotics 2019
