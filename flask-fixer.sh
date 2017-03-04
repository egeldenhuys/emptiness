#!/bin/bash

installDir=/mnt/dalla-hdd/dalla/emptiness

sleep 1800

while true
do
	echo "[$(date)] Fixing Flask..."
	$installDir/stop-flask.sh
	sleep 5
	$installDir/start-flask.sh
	sleep 1800
done
