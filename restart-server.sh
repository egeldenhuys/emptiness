#!/bin/bash

echo Restarting servers...

echo "---- Stopping ----"
./stop-server.sh
echo " "
echo "---- Starting ----"
./start-server.sh
