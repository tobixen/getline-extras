#!/usr/bin/python3

import os
import requests
import invest

auth=(os.environ['GETLINE_USERNAME'], os.environ['GETLINE_PASSWORD'])

investments=[
    (640, 0.02),
    (2, 0.2),
    (146, 0.04),
    (889, 0.04),
    (1168, 0.04),
    (36, 0.2),
    (16, 0.04),
    (127, 0.01),
    (5, 0.1),
    (177, 0.01),
    (894, 0.01),
    (136, 0.06),
    (2006, 0.06),
    (838, 0.01),
    (1925, 0.01),
    (620, 0.1),
    (1736, 0.2),
    (2022, 0.2),
    (1445, 0.2),
    (129, 0.2),
    (133, 0.1),
    (1511, 0.2),
    (2012, 0.1),
    (2572, 0.1),
    (1152, 0.1),
    (2434, 0.1)
    ]

tot_wanted_investments = sum([x[1] for x in investments])
## TODO: find my total and available balance and adjust the investments accordingly 

for user in investments:
    loans = requests.get('https://getline.in/api/v1/users/%i/loans/' % user[0], auth=auth).json()
    if not loans:
        continue
    max_intr = max([float(x['interest']) for x in loans])
    invest.invest(user[0], max_intr-0.00001, user[1])
