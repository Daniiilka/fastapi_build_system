#!/bin/bash

session="build-system"
tmux -S new-session -d -s $session
window=0
tmux -S rename-window -t $session:$window '5000-build-system'
tmux -S send-keys -t $session:$window 'cd {PATH TO THE PROJECT}' C-m
tmux -S send-keys -t $session:$window 'source venv/bin/activate' C-m
tmux -S send-keys -t $session:$window 'uvicorn main:app --reload --port 5000' C-m


