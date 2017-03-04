#!/bin/bash

# Flask server

port=6969
host=0.0.0.0
installDir=/mnt/dalla-hdd/dalla/emptiness

serverScript=$installDir/flask-server.py
pidFile=$installDir/flask-server.pid
logFile=$installDir/flask-server.log

if [ -f $pidFile ]; then
	echo Flask server is already running!

else
	echo Starting Flask server on $host:$port

	export FLASK_APP=$serverScript
	flask run --host=$host --port=$port >> $logFile 2>&1 &

	echo $! > $pidFile
	echo PID = $!
fi
