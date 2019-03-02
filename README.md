## Manual Control


### HOW TO RUN ROBOT

##### Laptop:
1. run ```python3 ManualControl.py``` 
2. note ip of laptop (i.e. ```ifconfig```)

##### Pi:
1. ssh into pi with 2 sessions
2. edit ManualControlState file with ip of laptop:
    ```nano ros_catkin_ws/src/robot/manual/src/ManualControlState.py```
    scroll and update ip with laptop ip
3. on first session: run ```rosrun manual serialLaunch.launch```
4. on second: run ```tmux```  
5. then:  ```./startScript``` to start  


##### sending commands:
On the laptop, type keys notes in ManualControl.py 
