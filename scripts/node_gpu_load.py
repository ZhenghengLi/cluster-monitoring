#!/usr/bin/env python3

import argparse
import subprocess
import xml
import json
import re
import psutil

parser = argparse.ArgumentParser(description='desc')
args = parser.parse_args()

ref_gpu_util = re.compile(r"""
GPU \s+ (\S+) \s+
Utilization \s+
Gpu    \s+ : \s+ (\d+\.?\d*) \s+ % \s+
Memory \s+ : \s+ (\d+\.?\d*) \s+ %
""", re.X)

nvidia_smi_output = str(subprocess.check_output(['nvidia-smi', '-q', '-d', 'UTILIZATION']), 'utf-8')

matches = re.findall(ref_gpu_util, nvidia_smi_output)

gpu_load = {}
for m in matches:
    gpu_load[m[0]] = {}
    gpu_load[m[0]]['gpu'] = float(m[1])
    gpu_load[m[0]]['mem'] = float(m[2])

print(json.dumps(gpu_load))
