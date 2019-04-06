## Manual Control


### HOW TO RUN ROBOT


##### Pi:
1. ssh into pi with 2 sessions ```ssh pi@192.168.1.45```
3. on first session: run ```roslaunch manual serialLaunch.launch``` to connect pi with arduinos

	Alternately, these are the commands for each node individually if the launch file errors. the port options are ACM0, ACM1, AMA0, AMA1; try each if errors persist
	```rosrun rosserial_python serial_node.py __name:=serial_node1 _baud:=9600 _port:=/dev/ttyACM0```
	and
	```rosrun rosserial_python serial_node.py __name:=serial_node2 _baud:=9600 _port:=/dev/ttyACM1```

4. on second run ```rosrun manual AlternateManualCommand.py``` 

Alternately, to view message & message feedback run:
     on second: run ```tmux```  
     then:  ```./startScript``` to start  & view message output

##### sending commands:
On the laptop, type a key + enter to send commands to robot according to the following:

```
'''
Key press       Command
 enter          stop all motors
 9              quit & exit 

 w              drive forward
 s              drive backwards
 a              turn in place left
 d              turn in place right
 p              pack in
 o              pack out

 r              raise bucket chain
 f              lower  bucket chain
 t              run bucket chain slow (reverse)
 y              run bucket chain fast with ramp up
 g		run bucket chain fast with ramp up while slowly lowering

 z              raise conveyor belt
 x		lower conveyor belt
 c		run coneyor belt
```
