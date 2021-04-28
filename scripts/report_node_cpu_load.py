#!/usr/bin/env python3

import argparse
import time
import os
import json
import subprocess
import requests
from multiprocessing import Pool
from datetime import datetime


parser = argparse.ArgumentParser(description='desc')
parser.add_argument("-i", dest="interval", type=int, default=1)
parser.add_argument("-r", dest="repeat", type=int, default=1)
parser.add_argument("--url", dest="url", type=str, default='http://localhost:3000/node-cpu-load')
parser.add_argument("--password", dest="password", type=str, default='xxxx')
args = parser.parse_args()

my_path = os.path.realpath(__file__)
my_folder = os.path.dirname(my_path)
script_path = os.path.join(my_folder, 'collect_node_cpu_load.py')

output = json.loads(subprocess.check_output([script_path, '-i', str(args.interval), '-r', str(args.repeat)]))

res = requests.post(args.url, json=output, headers={'authorization': args.password})

print(res.status_code)
print(res.text)
