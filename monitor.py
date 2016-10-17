#!/usr/bin/python2

import os
import urllib2
import json
import time
import sys

class DataComparator:
    def __init__(self):
        self.prev = None
        
    def iterate(self, f):
        data = json.load(f)
        investments = set([(x['name'],x['investment']['used']) for x in data])
        changeset = {}
        if self.prev:
            prev_ = self.prev-investments
            new_ = investments-self.prev
            for i in prev_:
                changeset[i[0]] = -i[1]
            for i in new_:
                changeset[i[0]] += i[1]
        self.prev = investments
        return changeset

    def report(self, changeset=None, f=None):
        if (changeset is None) and (f is not None):
            changeset = self.iterate(f)
        significants = [k for k in changeset if abs(changeset[k]> > 400000]
        if significants:
            print time.strftime('%F %H:%M:%S')
            print "DELTA INVESTMENTS:"
            try:
             for c in significants:
                print "%16s: %+.4f" % (c, float(changeset[c])/10**8)
            except:
                import pdb; pdb.set_trace()

obj = DataComparator()
if len(sys.argv)>1:
    for fname in sys.argv[1:]:
        with open(fname, 'r') as f:
            obj.report(f=f)
    sys.exit(0)

opener = urllib2.build_opener()
opener.addheaders.append(('Cookie', 'session='+os.environ['GETLINE_COOKIE']))
while True:
    d1 = time.time()
    f = opener.open("https://getline.in/api/v1/friends/")
    d2 = time.time()
    obj.report(f=f)
    ## sleep 200 times as long as we waited for the response, but minimum 10 seconds and maximum 600 seconds
    time.sleep(max(min(600,200*(d2-d1)),10))
