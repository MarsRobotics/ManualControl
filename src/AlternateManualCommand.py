#!/usr/bin/env python3
import sys
sys.path.append("/home/pi/ros_catkin_ws/src/robot/manual/src")
import rospy
import roslib

from manual.msg import SimpleCommand

roslib.load_manifest('manual')


'''
Key press       Command
 enter          stop all motors
 9              quit & exit 

 w              drive forward
 s              drive backwards
 a              turn articulation joints left
 d              turn articulation joints right
 p              pack in
 o              pack out

 r               raise bucket chain
 f               lower  bucket chain
 t               run bucket chain slow 
 y               run bucket chain fast with ramp up

 z              raise conveyor belt
 x              lower conveyor belt 
 c              run conveyor belt


 8             test function --runs back wheels & stops
'''


def get_commands():

    command = input("type command followed by enter:")

    if command == "":
        publish(7)
        print("stop all motors")
    elif command == 'w':
        publish(1)
        print("drive forward")
    elif command == 's':
        publish(2)
        print("drive backwards")
    elif command == 'a':
        publish(5)
        print("turn left")
    elif command == 'd':
        publish(6)
        print("turn right")
    elif command == 'p':
        publish(8)
        print("pack in")
    elif command == 'o':
        publish(9)
        print("pack out")
    elif command == 'r':
        publish(11)
        print('raise bucket chain')
    elif command == 'f':
        publish(12)
        print('lower bucket chain')
    elif command == 't':
        publish(10)
        print('run bucket chain slow')
    elif command == 'y':
        publish(16)
        print('run bucket chain ramp up')
    elif command == 'z':
        publish(13)
        print('raise conveyor')
    elif command == 'x':
        publish(14)
        print('lower conveyor')
    elif command == 'c':
        publish(15)
        print('run conveyor')
    elif command == '8':
        publish(999)
        print('test')
        publish(7)
    elif command == '9':
        publish(7)
        print("exit")
        exit()
    else:
        print('not a valid command')


def publish(command):
    movementPub.publish(
        data=command)
    return




if __name__ == "__main__":
    #start ros publisher
    movementPub = rospy.Publisher('MovementCommand', SimpleCommand, queue_size=10)
    rospy.init_node('manual', anonymous=True)

   #continuously recieve and publish commands
    while True:
        get_commands()
