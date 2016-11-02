#!/usr/bin/python3

import os
import requests

cookie={'session': os.environ['GETLINE_COOKIE']}

def invest(user_id, rate, limit):
    return requests.put('https://getline.in/api/v1/friends/%s/' % user_id, cookies=cookie, data = {'limit': limit*10**8, 'interest': rate})


