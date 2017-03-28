#!/usr/bin/python3

import os
import requests
import invest

auth=(os.environ['GETLINE_USERNAME'], os.environ['GETLINE_PASSWORD'])

print("foo")

investments=[
    (16, 0.04),
    (2, 0.3),
    (5, 0.1),
    (36, 0.4),
    (127, 0.01),
    (129, 0.2),
    (133, 0.1),
    (136, 0.06),
    (146, 0.04),
    (177, 0.01),
    (620, 0.1),
    (640, 0.02),
    (838, 0.01),
    (889, 0.04),
    (894, 0.01),
    (1152, 0.15),
    (1168, 0.04),
    (1201, 0.1),
    (1445, 0.2),
    (1511, 0.2),
    (1598, 0.3),
    (1736, 0.5),
    (1925, 0.01),
    (2006, 0.06),
    (2012, 0.1),
    (2022, 0.2),
    (2434, 0.1),
    (2572, 0.1),
    (2635, 0.05)
    ]

tot_wanted_investments = sum([x[1] for x in investments])
## TODO: find my total and available balance and adjust the investments accordingly 

for user in investments:
    try:
        loans = requests.get('https://getline.in/api/v1/users/%i/loans/' % user[0], auth=auth).json()
    except:
        loans = []
        #logging.warn ..
    if not [x for x in loans if not 'bot' in x['name']]:
        continue
    max_intr = max([float(x['interest']) for x in loans if not 'bot' in x['name']])
    try:
        invest.invest(user[0], max_intr-0.00001, user[1])
    except:
        pass
        #logging.warn ..
