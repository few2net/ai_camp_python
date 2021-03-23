from api import Turtlebot

robot = Turtlebot()
ir_left = robot.get_sensor(0)
ir_right = robot.get_sensor(1)
L_TH = 200
R_TH = 200

print("ir_left: " + str(ir_left))
if(ir_left<L_TH):
	print("ir_left is white")
else:
	print("ir_left is black")
	
print("ir_right: " + str(ir_right))
if(ir_right<R_TH):
	print("ir_right is white")
else:
	print("ir_right is black")
