#!/usr/bin/env python3

import subprocess
from urllib import request, parse
from datetime import datetime

mpstat_status = str(subprocess.check_output('/path/to/show_mpstat_mt'), 'utf-8')

cur_time = str(datetime.now())
mpstat_status = 'Updated Time: ' + cur_time + '\n' + mpstat_status

url = 'https://hostname/update_status.php'
values = {'password': 'xxxxxx', 'contents': mpstat_status}

data = parse.urlencode(values).encode()
req =  request.Request(url, data=data)
resp = request.urlopen(req)

the_page = str(resp.read(), 'utf-8')
print(the_page)
