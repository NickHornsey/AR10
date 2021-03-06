#!/usr/bin/env python
#Active8 Robots, AR10 Teleop_key node
#Beta release 1.1
#Written by Nick Hornsey
#Last edited on 11/10/16

#The following program can be used to publish to the "commands" topic to control the AR10 hand instead of using rostopic pub
#It can be opened from the ros workspace with the following commmand:
#rosrun ar10 ar10_teleop_node.py

import rospy
from std_msgs.msg import String

def talker():
    pub = rospy.Publisher('commands', String, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        command = raw_input("enter key >>").upper()
        rospy.loginfo(command)
        pub.publish(command)
        rate.sleep()

if __name__ == '__main__':
    print "\033c\n"
    print "Active8 Robots, AR10 Hand Demonstration"
    print "======================================="
    print
    print
    print "  P = Point Finger         O = Open Hand"
    print "  OK = 'OK' Pose           C = Close Hand"
    print "                           H = Hold Tennis Ball"
    print "                           G = Hold Golf Ball"
    print "  E = Exit                 D = Demonstrate Range of Motions " 

    print
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
