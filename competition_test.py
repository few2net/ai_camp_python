#!/usr/bin/env python

from api import Turtlebot
import time

print("start")
robot = Turtlebot()
L_TH = 50
R_TH = 40


state = 0
while(True):
    robot.detect()
    """
    ir_left = robot.get_sensor(0)
    ir_right = robot.get_sensor(1)
    print(ir_left,ir_right)


    if(ir_left>L_TH and ir_right>R_TH):
        robot.move_robot(30,30)

    elif(ir_left>L_TH and ir_right<R_TH):
        robot.move_robot(20,30)

    elif(ir_left<L_TH and ir_right>R_TH):
        robot.move_robot(30,20)
    """

