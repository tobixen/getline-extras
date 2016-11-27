#!/usr/bin/python3

import os
import requests

auth=(os.environ['GETLINE_USERNAME'], os.environ['GETLINE_PASSWORD'])

def invest(user_id, rate, limit):
    if limit<20: ## limit is surely given as bitcoins, not as satoshis.
        limit *= 10**8
        limit = int(limit)
    return requests.put('https://getline.in/api/v1/friends/%s/' % user_id, auth=auth, data = {'limit': limit, 'interest': rate})

