from api import Turtlebot
import time

robot = Turtlebot()
L_TH = 200
R_TH = 200

while(True):
	ir_left = robot.get_sensor(0)
	ir_right = robot.get_sensor(1)
	print(ir_left,ir_right)
	robot.move_robot(50,50)
	if(ir_left>L_TH and ir_right>R_TH):
		print("Stop")
		break
