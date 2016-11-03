#!/usr/bin/python3

import os
import requests

auth=(os.environ['GETLINE_USERNAME'], os.environ['GETLINE_PASSWORD'])

def invest(user_id, rate, limit):
    return requests.put('https://getline.in/api/v1/friends/%s/' % user_id, auth=auth, data = {'limit': int(limit*10**8), 'interest': rate})


