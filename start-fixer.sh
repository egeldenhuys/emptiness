#!/bin/bash

installDir=/mnt/dalla-hdd/dalla/emptiness

logFile=$installDir/flask-fixer.log
pidFile=$installDir/flask-fixer.pid

# Fixer
if [ -f $pidFile ]; then
	echo Fixer is already running!
else
	echo Starting Fixer daemon...

	$installDir/flask-fixer.sh >> $logFile 2>&1 &

	echo $! > $pidFile
	echo PID = $!
fi
