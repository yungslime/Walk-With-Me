#!/bin/bash
killall node
sleep 1
tmux kill-session -t log_window
