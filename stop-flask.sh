#!/bin/bash

# Flask server
if [ ! -f flask-server.pid ]; then
	echo "Flask server is not running (PID file not found)!"

else
	flaskPID=$(cat flask-server.pid)
	echo Killing Flask with PID $flaskPID
	kill -9 $flaskPID
	rm flask-server.pid
fi
