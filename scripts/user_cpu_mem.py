#!/usr/bin/env python3

import argparse
import time
import psutil

parser = argparse.ArgumentParser(description='desc')
parser.add_argument("-i", dest="interval", type=int, default=1)
args = parser.parse_args()

user_dict = {}
exclude_user = ['root', 'systemd-resolve', 'systemd-timesync']

proc: psutil.Process
for proc in psutil.process_iter():
    proc.cpu_percent()

time.sleep(args.interval)

for proc in psutil.process_iter():
    with proc.oneshot():
        user = proc.username()
        if user in exclude_user:
            continue
        cpu = proc.cpu_percent()
        mem = proc.memory_percent()
        if cpu + mem < 0.01:
            continue
        if user in user_dict:
            user_dict[user]['cpu'] += cpu
            user_dict[user]['mem'] += mem
        else:
            user_dict[user] = {}
            user_dict[user]['cpu'] = cpu
            user_dict[user]['mem'] = mem

print(user_dict)
