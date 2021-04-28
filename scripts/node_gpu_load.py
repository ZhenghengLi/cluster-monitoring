#!/usr/bin/env python3

import argparse
import subprocess
import xml
import json
import time
import re
import psutil

parser = argparse.ArgumentParser(description='desc')
parser.add_argument("-i", dest="interval", type=int, default=1)
parser.add_argument("-r", dest="repeat", type=int, default=1)
args = parser.parse_args()

ref_gpu_util = re.compile(r"""
GPU \s+ (\S+) \s+
Utilization \s+
Gpu    \s+ : \s+ (\d+\.?\d*) \s+ % \s+
Memory \s+ : \s+ (\d+\.?\d*) \s+ %
""", re.X)

gpu_load = {}

for x in range(args.repeat):
    time.sleep(args.interval)
    nvidia_smi_output = str(subprocess.check_output(['nvidia-smi', '-q', '-d', 'UTILIZATION']), 'utf-8')
    matches = re.findall(ref_gpu_util, nvidia_smi_output)
    for m in matches:
        if (m[0] in gpu_load):
            gpu_load[m[0]]['gpu'] += float(m[1])
            gpu_load[m[0]]['mem'] += float(m[2])
        else:
            gpu_load[m[0]] = {}
            gpu_load[m[0]]['gpu'] = float(m[1])
            gpu_load[m[0]]['mem'] = float(m[2])

gpu_load_list = []
for x in gpu_load:
    gpu_load[x]['gpu'] /= args.repeat
    gpu_load[x]['mem'] /= args.repeat
    gpu_load_list.append({'busid': x, 'util': gpu_load[x]})

print(json.dumps(gpu_load_list))
