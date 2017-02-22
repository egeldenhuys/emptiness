#!/bin/bash

# Fixer
if [ -f fixer.pid ]; then
	echo Fixer is already running!
else
	echo Starting Fixer daemon...

	./fixer.sh >> fixer.log 2>&1 &

	echo $! > fixer.pid
	echo PID = $!
fi
