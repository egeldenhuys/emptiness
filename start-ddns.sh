#!/bin/bash

# DNS Updater
if [ -f dns.pid ]; then
	echo DNS daemon is already running!
else
	echo Starting DNS update daemon...

	./dns.sh >> dns.log 2>&1 &

	echo $! > dns.pid
	echo PID = $!
fi
