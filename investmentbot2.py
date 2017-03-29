#!/usr/bin/python3

import os
import requests
import invest

auth=(os.environ['GETLINE_USERNAME'], os.environ['GETLINE_PASSWORD'])

print("foo")

investments=[
    (16, 0.02),
    (2, 0.3),
    (5, 0.3),
    (36, 0.4),
    (127, 0.005),
    (129, 0.3),
    (133, 0.1),
    (136, 0.05),
    (146, 0.04),
    (177, 0.01),
    (406, 0.3),
    (620, 0.1),
    (640, 0.04),
    (694, 0.08),
    (838, 0.01),
    (889, 0.05),
    (894, 0.01),
    (1152, 0.3),
    (1168, 0.05),
    (1201, 0.15),
    (1445, 0.2),
    (1511, 0.2),
    (1598, 0.3),
    (1736, 0.5),
    (1925, 0.01),
    (2006, 0.1),
    (2012, 0.07),
    (2022, 0.0),
    (2434, 0.1),
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
