#!/bin/sh

python3 main.py --url=https://wltest.dns-systems.net/ >> /dev/null && cat out.json
