#!/bin/bash

# DNS Updater
if [ ! -f dns.pid ]; then
	echo "DNS daemon is not running (PID file not found)!"

else
	dnsPID=$(cat dns.pid)
	echo Killing DNS daemon with PID $dnsPID
	kill -9 $dnsPID
	rm dns.pid
fi
