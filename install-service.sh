#!/bin/bash

sudo cp -f emptiness.service /etc/systemd/system/
sudo systemctl enable emptiness.service
sudo systemctl start emptiness.service
