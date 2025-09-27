#!/usr/bin/env python3


import rospy
from robot_fleet_manager.msg import custom
from pub import talker



if __name__ == '__main__' :

    rospy.init_node("listener")
    
    rospy.Subscriber("custom_message" , custom , callback= talker)

    rospy.loginfo("message is received  !!!")

    rospy.spin()