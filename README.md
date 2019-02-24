## Manual Control

server: 

-contains python file(s) to be run from laptop

src:
- code to run on pi with following commands

1. Start communication with arduino (port may vary, also try ttyACM1, ttyAMA0, ttyAMA1)
```rosrun rosserial_python serial_node.py _port:=/dev/ttyACM0 _baud:=9600``

2. **optional: to see message output **
Commands sent from pi to arduino
``` rostopic echo MovementCommand```
response from arduino to pi
```rostopic echo MovementFeedback```

3. From Laptop
set up listening server on laptop
```python ManualControl.py```

4. on pi:
edit the ManualControlState file with correct ip:

``` nano /ros_catkin_ws/src/robot/manual/src/ManualControlState.py```
and change the self.HOST parameter to the laptop ip

5. on pi:
run the ManualControlState file using the manual ros packages
```rosrun manual ManualControlState.py```
