## Manual Control


### HOW TO RUN ROBOT

##### Laptop:
1. run ```python3 ManualControl.py``` 
2. note ip of laptop (i.e. ```ifconfig```)

##### Pi:
1. ssh into pi with 2 sessions
2. on first : run ```rosrun manual serialLaunch.launch```
3. on second: run ```tmux```  
4. then:  ```./startScript``` to start  


##### sending commands:
On the laptop, type keys notes in ManualControl.py 
