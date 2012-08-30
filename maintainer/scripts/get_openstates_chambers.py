#!/usr/bin/env python

from collections import defaultdict
from sunlight import openstates
import json
import sys

obj = json.load(open(sys.argv[1], 'r'))
ret = defaultdict(list)

ret = defaultdict(list)

for state in obj:
    inf = obj[state]
    upper_c = len(inf['upper'])
    lower_c = len(inf['lower'])

    if upper_c > 0:
        ret[state].append({
            "name": "upper",
            "count": upper_c
        })

    if lower_c > 0:
        ret[state].append({
            "name": "lower",
            "count": lower_c
        })

print json.dumps(ret)
