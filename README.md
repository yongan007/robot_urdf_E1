## ROS test

# unitest
This unitest is for check about correctness of a forward kinematics script.

filename : fk.py

tester: fk_test.py
 
To run unintest: 

	rosrun rostest fk_test.py

## Integration test

This is intergration test show if robot get right angle from control publisher. So I created a subscriber to read the joint state. After that we can compare the angle from publisher with subscriber.

To check angle from subscriber:
	
	rosrun asimo_control control.py

To check angle from publisher:
	
	rosrun asimo joint_state_subscriber.py

To run integration test: 
	
	rosrun rostest joint_integration_test.py

## Video 

[![Watch the video]](https://www.youtube.com/watch?v=D0a5ea_kOAI)

[![IMAGE ALT TEXT HERE](http://img.youtube.com/vi/D0a5ea_kOAI/0.jpg)](https://www.youtube.com/watch?v=D0a5ea_kOAI)

Created with ROS melodic 
