
from pynput.keyboard import Key, Listener, KeyCode
import socket
#!/usr/bin/env python3
try:
    import cPickle as pickle
except ImportError:
    import pickle

from socket import error as socket_error

# How big of a string should we use to send the data body size
BODY_SIZE_STRING_SIZE = 50
from DataTransferProtocol import sendData #this is fine
import time

class MovementData:

    def __init__(self):
        self.serialID = 0
        self.driveDirection = 0
        self.stop = 0
        self.packIn = 0
        self.packOut = 0
        self.raiseBucketChain = 0
        self.lowerBucketChain = 0
        self.speedBucketChain = 0
        self.raiseConveyorBelt = 0
        self.lowerConveyorBelt = 0
        self.speedConveyorBelt = 0
        self.misc1 = 0
        self.misc2 = 0
        return
'''
Key press       Command
 space           stop all motors
 q               quit & exit
 
 i               pack in
 o               pack out
 
 up arrow        drive forward
 down arrow      drive backwards
 left arrow      turn left & drive forward
 right arrow     turn right & drive forward
 
 a               turn articulation joints left (don't move drive motors)
 d               turn articulation joints right (don't move drive motors) 
 6               drive direction 6
 
 r               raise bucket chain
 l               lower  bucket chain
 t               turn bucket chain
 
 c              turn conveyor belt
'''

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("",30003))
print("binding")
s.listen(1)
print("listening")
(sock,address) = s.accept()
print("accepted connection")



def on_press(key):
    data = MovementData()

    if key == Key.space:
        data.stop = 1
        sendData(sock, data)
        time.sleep(.1)
        print("STOP")
        sendData(sock, data)
    elif key == KeyCode.from_char('q'):
        print("exit")
        data.stop = 1
        sendData(sock, data)
        sock.shutdown(socket.SHUT_RDWR)
        sock.close()
        s.shutdown(socket.SHUT_RDWR)
        s.close()
        exit()
    elif key == KeyCode.from_char('i'):
        data.packIn = 1
        print("pack in")
        sendData(sock, data)
    elif key == KeyCode.from_char('o'):
        data.packOut = 1
        print("pack out")
        sendData(sock, data)
    elif key == Key.up:
        data.driveDirection = 1
        print("drive forward")
        sendData(sock, data)
    elif key == Key.down:
        data.driveDirection = 2
        print("drive backward")
        sendData(sock, data)
    elif key == Key.left:
        data.driveDirection = 3
        print("drive left and forward")
        sendData(sock, data)
    elif key == Key.right:
        data.driveDirection = 4
        print("drive right and forward")
        sendData(sock, data)
    elif key == KeyCode.from_char('a'):
        data.driveDirection = 5
        print("articulate left")
        sendData(sock, data)
    elif key == KeyCode.from_char('d'):
        data.driveDirection = 6
        print("articulate right")
        sendData(sock, data)
    else:
        print("Not a valid command")
        return

def on_release(key):
    if key == Key.esc:
        data = MovementData()
        sendData(sock, data)
        time.sleep(2)
        sock.shutdown(socket.SHUT_RDWR)
        sock.close()
        s.shutdown(socket.SHUT_RDWR)
        s.close()
        return False

with Listener(on_press=on_press, on_release=on_release) as l:
    l.join()
