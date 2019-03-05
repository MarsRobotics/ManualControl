## Manual Control


### HOW TO RUN ROBOT


##### Pi:
1. ssh into pi with 2 sessions ```ssh pi@192.168.1.45```
3. on first session: run ```roslaunch manual serialLaunch.launch``` to connect pi with arduinos
4. on second run ```rosrun manual AlternateManualCommand.py``` 

or to view message & message feedback run:
     on second: run ```tmux```  
     then:  ```./startScript``` to start  & view message output

##### sending commands:
On the laptop, type a key + enter to send commands to robot according to the following:

```
Key press      Command
 enter          stop all motors
 9              quit & exit 

 w              drive forward
 s              drive backwards
 a              turn articulation joints left
 d              turn articulation joints right


 r               raise bucket chain
 f               lower  bucket chain
 t               run bucket chain slow 
 y               run bucket chain fast with ramp up

 z              raise conveyor belt !not yet tested!!
 x              lower conveyor belt !not yet tested!!
 c              run conveyor belt   !not yet tested!!


 8             test function --runs back wheels & stops
```