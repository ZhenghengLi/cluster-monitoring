#!/usr/bin/env python3

import argparse
import time
import json
import subprocess
import requests
from multiprocessing import Pool
from datetime import datetime

password = 'xxxx'

parser = argparse.ArgumentParser(description='desc')
parser.add_argument("-i", dest="interval", type=int, default=1)
parser.add_argument("-r", dest="repeat", type=int, default=1)
parser.add_argument("--url", dest="url", type=str, default='http://localhost:3000/node-cpu-load')
args = parser.parse_args()

script_path = "/home/mark/GitHub/cluster-monitoring/scripts/collect_node_cpu_load.py"
output = json.loads(subprocess.check_output([script_path, '-i', str(args.interval), '-r', str(args.repeat)]))

res = requests.post(args.url, json=output, headers={'authorization': password})

print(res.status_code)
print(res.text)
