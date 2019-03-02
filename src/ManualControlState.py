#!/usr/bin/env python3
import sys
sys.path.append("/home/pi/ros_catkin_ws/src/robot/manual/src")

import rospy
import roslib
import time
import socket
import sys

try:
    import cPickle as pickle
except ImportError:
    import pickle

from socket import error as socket_error

from MovementData import MovementData

from DataTransferProtocol import receiveData, sendData

from manual.msg import MovementCommand
from manual.msg import MovementFeedback
from manual.msg import ImageProc
from manual.msg import SimpleCommand

roslib.load_manifest('manual')


# How big of a string should we use to send the data body size
BODY_SIZE_STRING_SIZE = 50


class ManualControlData:

    def __init__(self):
        self.data = 0
        return


#track current state and program
class StateMachine():

    #init robot
    def __init__(self):
        self.manual = True

    #control program
    def startRobot(self):
        self.HOST = "192.168.1.140"  # laptop IP
        self.PORT = 30003  # communication port

        # connect to laptop (note: laptop program is server so must start laptop program first)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("attempt to connect manual")
        s.connect((self.HOST, self.PORT))
        print("connected manual")
        self.sock = s
        movementPub = self.rosSetup()
        print("ros publisher set up")

        self.sock.setblocking(1)
       	while True:
            manualCommand = receiveData(self.sock)
            c = ManualControlData()
            c.data = manualCommand.data
            print("received new command")
            movementPub.publish(
                data=c.data)
            print("published command to arduino")
           

    # ros node for program and publisher for movement commands
    def rosSetup(self):
        # create ros publisher to update/send data
        movementPub = rospy.Publisher('MovementCommand', SimpleCommand, queue_size=10)
        rospy.init_node('manual', anonymous=True)
        return (movementPub)


# PROGRAM ENTRY
if __name__ == "__main__":

    sm = StateMachine()
    sm.startRobot()
