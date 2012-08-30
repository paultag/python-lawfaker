#!/usr/bin/env python

import json
import sys

lines = open(sys.argv[1], 'r').readlines()

order = [
    "name",
    "rank",
    "count"
]

ret = []

for line in lines:
    info = line.split(",")
    metainf = {}
    for o in range(0, len(order)):
        metainf[order[o]] = info[o]
    ret.append({
        "name": metainf['name'],
        "count": metainf['count']
    })

print json.dumps(ret)
