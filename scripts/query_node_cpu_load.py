#!/usr/bin/env python3

import argparse
import time
import json
import requests

default_max_time = round(time.time() * 1000)
default_min_time = default_max_time - 3 * 60 * 1000

parser = argparse.ArgumentParser(description='desc')
parser.add_argument("--url", dest="url", type=str, default='http://localhost:3000/node-cpu-load')
parser.add_argument("--minTime", dest="minTime", type=int, default=default_min_time)
parser.add_argument("--maxTime", dest="maxTime", type=int, default=default_max_time)
parser.add_argument("--password", dest="password", type=str, default='xxxx')
args = parser.parse_args()

query_obj = {
    'where': {
        'time': {
            'between': [args.minTime, args.maxTime]
        }
    }
}

url = args.url + '?filter=' + requests.utils.quote(json.dumps(query_obj))
res = requests.get(url, headers={'authorization': args.password})

print(res.status_code)
print(res.text)
