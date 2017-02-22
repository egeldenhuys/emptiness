#!/bin/bash

echo Restarting servers...

echo "---- Stopping ----"
./stop-all.sh

echo " "
echo "---- Starting ----"
./start-all.sh
