#!/usr/bin/env python

from sunlight import openstates
import json
import sys

obj = json.load(open(sys.argv[1], 'r'))
ret = []

for state in obj:
    inf = obj[state]
    total = len(inf['upper']) + len(inf['lower'])
    ret.append({
        "name": state,
        "count": total
    })

print json.dumps(ret)
