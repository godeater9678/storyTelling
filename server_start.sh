#!/usr/bin/env bash
pkill -f main.py

nohup /usr/src/Python-3.10.12/python ./main.py --profile=local > /dev/null 2>&1 &

exit 0


