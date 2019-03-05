### How to update pi with current code 
(without internet connection on pi)

#### laptop side:
1. Update ManualControl repo from git (i.e. git pull) 

2. move files from laptop to pi:
    ```scp ManualControl/src/AlternateManualCommand.py pi@192.168.1.45:/home/pi/ros_catkin_ws/src/robot/manual/src```
    ```scp startScript.sh pi@192.168.1.45:/home/pi/```
    

3. ssh into pi ```ssh pi@192.168.1.45```
#### pi side (through ssh connection you just established)

3. make new file executable:
```chmod +x ros_catkin_ws/src/robot/manual/src/AlternateManualCommand.py```

#### troubleshooting
If the ```rosrun manual AlternateManualCommand.py``` fails, run a catkin_make to remake the library to include the new file:
```cd rosr_catkin_ws && catkin_make``` 



