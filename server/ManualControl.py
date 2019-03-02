
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
        self.data = 0
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
 
 r               raise bucket chain
 l               lower  bucket chain
 t               turn bucket chain
 
 c              turn conveyor belt
 f              raise conveyor belt
 v              lower conveyor belt 
 
 
 9              test function
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
        data.data = 7
        sendData(sock, data)
        time.sleep(.1)
        print("STOP")
        sendData(sock, data)
    elif key == KeyCode.from_char('q'):
        print("exit")
        data.data = 7
        sendData(sock, data)
        sock.shutdown(socket.SHUT_RDWR)
        sock.close()
        s.shutdown(socket.SHUT_RDWR)
        s.close()
        exit()
    elif key == KeyCode.from_char('i'):
        data.data = 8
        print("pack in")
        sendData(sock, data)
    elif key == KeyCode.from_char('o'):
        data.data = 9
        print("pack out")
        sendData(sock, data)
    elif key == Key.up:
        data.data = 1
        print("drive forward")
        sendData(sock, data)
    elif key == Key.down:
        data.data = 2
        print("drive backward")
        sendData(sock, data)
    elif key == Key.left:
        data.data = 3
        print("drive left and forward")
        sendData(sock, data)
    elif key == Key.right:
        data.data = 4
        print("drive right and forward")
        sendData(sock, data)
    elif key == KeyCode.from_char('a'):
        data.data = 5
        print("articulate left")
        sendData(sock, data)
    elif key == KeyCode.from_char('d'):
        data.data = 6
        print("articulate right")
        sendData(sock, data)
    elif key == KeyCode.from_char('r'):
        data.data = 11
        print("raise bucket chain")
        sendData(sock, data)
    elif key == KeyCode.from_char('l'):
        data.data = 12
        print("lower bucket chain")
        sendData(sock, data)
    elif key == KeyCode.from_char('t'):
        data.data = 10
        print("turn bucket chain")
        sendData(sock, data)
    elif key == KeyCode.from_char('c'):
        data.data = 15
        print("turn conveyor belt")
        sendData(sock, data)
    elif key == KeyCode.from_char('f'):
        data.data = 13
        print("raise conveyor belt")
        sendData(sock, data)
    elif key == KeyCode.from_char('v'):
        data.data = 14
        print("lower conveyor belt")
        sendData(sock, data)
    elif key == KeyCode.from_char('9'):
        data.data = 999
        print("test function ")
        sendData(sock, data)

    else:
        print("Not a valid command")



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
