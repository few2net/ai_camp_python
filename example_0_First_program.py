from api import Turtlebot
import time

robot = Turtlebot()
print("Hello world!")
while(True):
	robot.move_robot(10,10)
