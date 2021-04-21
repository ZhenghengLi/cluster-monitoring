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
args = parser.parse_args()

user = 'lizhh1'
node_list = ['cu01', 'cu02', 'cu03', 'cu04', 'gpu01', 'gpu02', 'gpu03', 'gpu04']
script_path = '/data-ib/home/lizhh1/workspace/cluster-monitoring/scripts/user_cpu_mem.py'


def remote_status(server: str):
    status = str(subprocess.check_output(['ssh', '%s@%s' % (user, server),
                                          script_path, '-i', str(args.interval), '-r', str(args.repeat)]), 'utf-8')
    return (server, status)


pool = Pool(len(node_list))
status_list = pool.map(remote_status, node_list)

print(json.dumps(status_list), end='')
