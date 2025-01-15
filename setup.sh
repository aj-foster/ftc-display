#!/bin/bash

sudo apt install --yes xdotool

cp ftc-scoring-display.py /home/pi/ftc-scoring-display.py
chmod +x /home/pi/ftc-scoring-display.py

mkdir -p /home/pi/.config/autostart
cp ftc-scoring-display.desktop /home/pi/.config/autostart/ftc-scoring-display.desktop
