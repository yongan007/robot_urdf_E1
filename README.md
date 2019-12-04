

![GitHub repo size](https://img.shields.io/github/repo-size/yongan007/robot_urdf_E1)  ![GitHub followers](https://img.shields.io/github/followers/yongan007?style=social)

[![welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://travis-ci.org/yongan007/robot_urdf_E1)   [![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)


## ROS test

 [![Build Status](https://travis-ci.org/yongan007/robot_urdf_E1.svg?branch=travis_ci)](https://travis-ci.org/yongan007/robot_urdf_E1) 

# unitest

This unitest is for check about correctness of a forward kinematics script.

filename : fk.py

tester: fk_test.py
 
To run unintest: 

	rosrun rostest fk_test.py

## Integration test

This is intergration test show if robot get right angle from control publisher. So I created a subscriber to read the joint state. After that we can compare the angle from publisher with subscriber.

To check the joint value from publisher:

	rosrun asimo_control control.py

To check the joint value from subscriber:

	rosrun rostest joint_state_subscriber.py

To run integration test: 
	
	rosrun rostest joint_integration_test.py


## Video 

#Ros sensor

[![Watch the video]](https://www.youtube.com/watch?v=_ndAP1dwUtQ)

#Ros control

[![IMAGE ALT TEXT HERE](http://img.youtube.com/vi/D0a5ea_kOAI/0.jpg)](https://www.youtube.com/watch?v=D0a5ea_kOAI)

[![IMAGE ALT TEXT HERE](http://img.youtube.com/vi/IKFGcrc6w74/0.jpg)](http://www.youtube.com/watch?v=IKFGcrc6w74)

#Ros test

[![IMAGE ALT TEXT HERE](http://img.youtube.com/vi/_ndAP1dwUtQ/0.jpg)](https://www.youtube.com/watch?v=_ndAP1dwUtQ)


