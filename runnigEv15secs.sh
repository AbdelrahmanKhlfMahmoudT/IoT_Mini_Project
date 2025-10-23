#!/bin/bash
while true; do
    python3 mqtt-code.py 2>&1
    sleep 15
done &
