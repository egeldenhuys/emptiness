#!/bin/bash

port=6969
host=0.0.0.0

# Flask server
if [ -f flask-server.pid ]; then
	echo Flask server is already running!

else
	echo Starting Flask server on $host:$port

	export FLASK_APP=flask-server.py
	flask run --host=$host --port=$port >> flask-server.log 2>&1 &

	echo $! > flask-server.pid
	echo PID = $!
fi

# DNS Updater
if [ -f dns.pid ]; then
	echo DNS daemon is already running!
else
	echo Starting DNS update daemon...

	./dns.sh >> dns.log 2>&1 &

	echo $! > dns.pid
	echo PID = $!
fi
