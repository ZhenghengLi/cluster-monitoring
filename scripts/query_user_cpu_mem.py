#!/usr/bin/env python3

import argparse
import time
import json
import requests

password = 'xxxx'

parser = argparse.ArgumentParser(description='desc')
parser.add_argument("--url", dest="url", type=str, default='http://localhost:3000/user-cpu-mem')
args = parser.parse_args()

query_obj = {
    'where': {
        'completed': False
    }
}

url = args.url + '?filter=' + requests.utils.quote(json.dumps(query_obj))
res = requests.get(url, headers={'authorization': password})

print(res.status_code)
print(res.text)
