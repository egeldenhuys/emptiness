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

# DNS Updater
if [ ! -f dns.pid ]; then
	echo "DNS daemon is not running (PID file not found)!"

else
	dnsPID=$(cat dns.pid)
	echo Killing DNS daemon with PID $dnsPID
	kill -9 $dnsPID
	rm dns.pid
fi
