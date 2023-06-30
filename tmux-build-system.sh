#!/bin/bash

session="build-system"
tmux -S new-session -d -s $session
window=0
tmux -S rename-window -t $session:$window '8502-sharing-styles'
tmux -S send-keys -t $session:$window 'cd {PATH TO THE PROJECT}' C-m
tmux -S /home/dev/socket send-keys -t $session:$window 'source venv/bin/activate' C-m
tmux -S /home/dev/socket send-keys -t $session:$window 'uvicorn main:app --reload --port 5000' C-m


