#!/bin/bash

installDir=/mnt/dalla-hdd/dalla/emptiness

logFile=$installDir/flask-fixer.log
pidFile=$installDir/flask-fixer.pid

# Kill Fixer
if [ ! -f $pidFile ]; then
	echo "Fixer is not running (PID file not found)!"

else
	pid=$(cat $pidFile)
	echo Killing Fixer with PID $pid
	kill -9 $pid
	rm $pidFile
fi
