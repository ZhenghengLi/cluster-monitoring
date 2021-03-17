#!/usr/bin/env python3

import subprocess
from urllib import request, parse
from datetime import datetime

usertop_status = str(subprocess.check_output('/path/to/bin/user_top_all'), 'utf-8')

cur_time = str(datetime.now())
usertop_status = 'Updated Time: ' + cur_time + '\n' + usertop_status

url = 'https://hostname/update_status.php'
values = {'password': 'xxxxxx', 'contents': usertop_status}

data = parse.urlencode(values).encode()
req =  request.Request(url, data=data)
resp = request.urlopen(req)

the_page = str(resp.read(), 'utf-8')
print(the_page)
