import rospy
import time
import threading
import os
from ros_vision.vision import vision
from geometry_msgs.msg import Twist
from std_msgs.msg import Int32MultiArray

MAX_LN_SPEED = 0.26  # constant max linear speed 0.26

class Turtlebot:
    def __init__(self):
        rospy.init_node('commander', anonymous=True)
        self.vel_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
        
        rospy.Subscriber("/infrared_topic", Int32MultiArray, self.sensor_callback)

        self.old_vel = Twist()
        self.current_vel = Twist()
        
        self.motor_thread = threading.Thread(target=self.publisher_thread)
        self.motor_thread.start()
        self.rate = rospy.Rate(200)
        rospy.sleep(1)  # set some delay for node settling
        
    def publisher_thread(self):
        time.sleep(1)
        while(not rospy.is_shutdown()):
            for i in threading.enumerate():
                if(i.name == 'MainThread' and not i.is_alive()):
                    return
            self.vel_pub.publish(self.current_vel)
            self.rate.sleep()
        print("exit")
        os._exit(0)

    def sensor_callback(self, msg):
        self.sensor_msg = msg

    def get_sensor(self, number_sensor=0):
        if self.sensor_msg!= None:
            return self.sensor_msg.data[number_sensor]
        else:
            return 0

    def start_camera(self):
        self.detector = vision()
    
    def detect_label(self):
        return self.detector.get_prediction()[0]

    def detect_score(self):
        return self.detector.get_prediction()[1]

    def move_robot(self, left, right):
        data = Twist()
        distance = 15.0 # distance from body to wheels
        linear_x = (left + right) / 100.0 * MAX_LN_SPEED/2.0  # summation of speed of each wheel=200%, so we divide it by 2
        angular_z = -(left - right) / float(distance)  # Ensure distance is float
        data.linear.x = linear_x
        data.linear.y = 0.0
        data.linear.z = 0.0
        data.angular.x = 0.0
        data.angular.y = 0.0
        data.angular.z = angular_z
        self.current_vel = data

    def stop(self):
        data = Twist()
        data.linear.x = 0.0
        data.linear.y = 0.0
        data.linear.z = 0.0
        data.angular.x = 0.0
        data.angular.y = 0.0
        data.angular.z = 0.0
        self.current_vel = data
