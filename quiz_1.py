from api import Turtlebot

robot = Turtlebot()
ir_left = robot.get_sensor(0)
ir_right = robot.get_sensor(1)
print("Infrared sensor left:" + str(ir_left))
print("Infrared sensor right:" + str(ir_right))
