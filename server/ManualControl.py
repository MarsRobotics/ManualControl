
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
 space           stop everything, cancelling current execution
 p               pack in
 d               pack out
 0               pause
 1               drive direction 1
 2               drive direction 2
 3               drive direction 3
 4               drive direction 4
 5               drive direction 5
 6               drive direction 6
 7               send test message
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

    if key == KeyCode.from_char('0'):
        sendData(sock, data)
        time.sleep(.1)
        data.pause = 0
        print("pause")
        sendData(sock, data)
    elif key == KeyCode.from_char('1'):
        data.driveDirection = 1
        print("drive direction is 1")
        sendData(sock, data)
    elif key == KeyCode.from_char('2'):
        data.driveDirection = 2
        print("drive direction is 2")
        sendData(sock, data)
    elif key == KeyCode.from_char('7'):
        data.driveDirection = 1
        print("sent a test message")
        sendData(sock, data)
    elif key == KeyCode.from_char('q'):
        print("sssstop")
        sendData(sock, data)
        sock.shutdown(socket.SHUT_RDWR)
        sock.close()
        s.shutdown(socket.SHUT_RDWR)
        s.close()
        exit()
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
