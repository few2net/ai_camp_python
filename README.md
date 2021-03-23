# AI_camp_python
This repo was tested on Raspberry pi 3B+ as a computer for student.

## Ros setup
Follow this instruction http://wiki.ros.org/ROSberryPi/Installing%20ROS%20Kinetic%20on%20the%20Raspberry%20Pi 


> Note: To avoid the memory exhaustion problem on Raspberry pi 3B+, you should [increase swap memory](https://nebl.io/neblio-university/enabling-increasing-raspberry-pi-swap/) before catkin_make. <br>I set it to 1024M.
 

## Geany IDE with python2.7
There are few configs to change before execute program.

#### Change terminal
1. Go to `Edit/Prereferences/Tools`
2. In Terminal box. Change from `x-terminal-emulator -e "/bin/sh %c"` to `x-terminal-emulator -e /bin/bash %c`

#### Change build command
1. Create new python file or Open `example_0_First_program.py`
2. Go to `Build/Set Build Commands`
3. In Execute box. Change from `python "%f"` to `source ~/ai_camp_python/env.bash && python2.7 "%f"`

#### ROS setting for Geany
You have to change `ROS_IP` and `ROS_MASTER_URI` in **ai_camp_python/env.bash** corresponding to your machine.
