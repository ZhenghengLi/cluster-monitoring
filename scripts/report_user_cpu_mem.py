#!/usr/bin/env python3

import argparse
import time
import json
import subprocess
from multiprocessing import Pool
from datetime import datetime

parser = argparse.ArgumentParser(description='desc')
parser.add_argument("-i", dest="interval", type=int, default=1)
parser.add_argument("-r", dest="repeat", type=int, default=1)
parser.add_argument("--url", dest="url", type=str, default=1)
args = parser.parse_args()

script_path = "/home/mark/GitHub/cluster-monitoring/scripts/collect_user_cpu_mem.py"
output = json.loads(subprocess.check_output([script_path, '-i', str(args.interval), '-r', str(args.repeat)]))

print(json.dumps(output))
