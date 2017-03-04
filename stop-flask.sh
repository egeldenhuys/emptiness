#!/bin/bash

installDir=/mnt/dalla-hdd/dalla/emptiness

serverScript=$installDir/flask-server.py
pidFile=$installDir/flask-server.pid
logFile=$installDir/flask-server.log

# Flask server
if [ ! -f $pidFile ]; then
	echo "Flask server is not running (PID file not found)!"

else
	flaskPID=$(cat $pidFile)
	echo Killing Flask with PID $flaskPID
	kill -9 $flaskPID
	rm $pidFile
fi
