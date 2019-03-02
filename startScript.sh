#!/bin/bash  
tmux start-server
tmux new-session  
tmux splitw -v -p 50
tmux selectp -t 1 
tmux splitw -h -p 50
tmux splitw -h -p 50
tmux selectp -t 0
tmux splitw -h -p 50
tmux selectp -t 0
tmux send-keys -t 1 "rosrun manual ManualControlState.py" C-m
tmux send-keys -t 2 "rostopic echo "MovementCommand"" C-m
tmux send-keys -t 3 "rostopic echo "MovementFeedback"" C-m
tmux send-keys -t 4 "rostopic echo "MovementFeedback"" C-m

