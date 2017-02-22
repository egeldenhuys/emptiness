#!/bin/bash

sleep 1800

while true
do
	echo "[$(date)] Fixing Flask..."
	./stop-flask.sh
	./start-flask.sh
	sleep 1800
done
