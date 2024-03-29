#!/usr/bin/env python3

import argparse
import time
import json
import os
import subprocess
from multiprocessing import Pool
from datetime import datetime

parser = argparse.ArgumentParser(description='desc')
parser.add_argument("-i", dest="interval", type=int, default=1)
parser.add_argument("-r", dest="repeat", type=int, default=1)
args = parser.parse_args()

user = 'lizhh1'
node_list = ['gpu01', 'gpu02', 'gpu03', 'gpu04', 'gpu05']

script_dir = os.path.dirname(os.path.abspath(__file__))
script_path = os.path.join(script_dir, 'node_gpu_load.py')

def remote_output(server: str):
    output = subprocess.check_output(['ssh', '%s@%s' % (user, server),
                                      script_path, '-i', str(args.interval), '-r', str(args.repeat)])
    return {'node': server, 'data': json.loads(output)}


pool = Pool(len(node_list))
status_list = pool.map(remote_output, node_list)

print(json.dumps(status_list))
