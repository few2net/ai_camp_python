#!/usr/bin/env python

from api import Turtlebot
import time

print("start")
robot = Turtlebot()
robot.start_camera()
L_TH = 50
R_TH = 40


state = 0
while(True):
    
    label = robot.detect_label()
    print("class: "+str(label))
    ir_left = robot.get_sensor(0)
    ir_right = robot.get_sensor(1)
    print(ir_left,ir_right)

    if(label == 1):
        robot.stop()
        time.sleep(2)
    if(ir_left>L_TH and ir_right>R_TH):
        robot.move_robot(30,30)

    elif(ir_left>L_TH and ir_right<R_TH):
        robot.move_robot(20,30)

    elif(ir_left<L_TH and ir_right>R_TH):
        robot.move_robot(30,20)


