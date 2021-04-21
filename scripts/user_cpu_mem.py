#!/usr/bin/env python3

import argparse
import time
import json
import psutil

parser = argparse.ArgumentParser(description='desc')
parser.add_argument("-i", dest="interval", type=int, default=1)
parser.add_argument("-r", dest="repeat", type=int, default=1)
args = parser.parse_args()

user_dict = {}
exclude_users = ['root', 'systemd-resolve', 'systemd-timesync']

my_pid = psutil.Process().pid

proc: psutil.Process
for proc in psutil.process_iter():
    proc.cpu_percent()

for x in range(args.repeat):
    time.sleep(args.interval)
    for proc in psutil.process_iter():
        with proc.oneshot():
            if proc.pid == my_pid:
                continue
            user = proc.username()
            if user in exclude_users:
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

for user in list(user_dict):
    user_dict[user]['cpu'] /= args.repeat * psutil.cpu_count()
    user_dict[user]['mem'] /= args.repeat
    if user_dict[user]['cpu'] < 0.1 or user_dict[user]['mem'] < 0.1:
        del user_dict[user]

print(json.dumps(user_dict))
