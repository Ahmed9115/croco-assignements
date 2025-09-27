#!/usr/bin/env python3

import rospy
from robot_fleet_manager.msg import custom


def talker(msg):

  rospy.loginfo(msg)



if __name__ == '__main__' :
    
      
      rospy.init_node('talker') 
      rospy.loginfo("message is sent !!!")
      
      pub = rospy.Publisher("custom_message" ,custom ,queue_size = 10)
      rate = rospy.Rate(10)
      
      msg = custom()
      msg.name ='Ahmed_robot'
      msg.battery = 54
      
      while not rospy.is_shutdown():
        pub.publish(msg)
        rate.sleep()

      
