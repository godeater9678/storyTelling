#!/usr/bin/env bash
pkill -f main.py
source venv/bin/activate
nohup python ./main.py --profile=local > /dev/null 2>&1 &

exit 0


