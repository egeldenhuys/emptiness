#!/bin/bash

# Kill Fixer
if [ ! -f fixer.pid ]; then
	echo "Fixer is not running (PID file not found)!"

else
	pid=$(cat fixer.pid)
	echo Killing Fixer with PID $pid
	kill -9 $pid
	rm fixer.pid
fi
