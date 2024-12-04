#!/usr/bin/env bash
pkill -f main.py

nohup python3 ./main.py --profile=local > /dev/null 2>&1 &

exit 0


