#!/usr/bin/env python3

import argparse
import time
import json
import psutil

parser = argparse.ArgumentParser(description='desc')
parser.add_argument("-i", dest="interval", type=int, default=1)
parser.add_argument("-r", dest="repeat", type=int, default=1)
args = parser.parse_args()

psutil.cpu_times_percent()

attr_list = ['user', 'system', 'idle', 'iowait', 'irq', 'softirq', 'steal', 'guest']

cpu_load = {}
for attr in attr_list:
    cpu_load[attr] = 0.0

cpu_load['mem'] = 0.0

for x in range(args.repeat):
    time.sleep(args.interval)
    ctp = psutil.cpu_times_percent()
    for attr in attr_list:
        cpu_load[attr] += getattr(ctp, attr)
    svm = psutil.virtual_memory()
    cpu_load['mem'] += svm.percent

for attr in cpu_load:
    cpu_load[attr] /= args.repeat

print(json.dumps(cpu_load))
