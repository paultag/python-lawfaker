#!/usr/bin/env python

from collections import defaultdict
from sunlight import openstates
import json
import sys

obj = json.load(open(sys.argv[1], 'r'))
ret = defaultdict(list)

ret = defaultdict(list)

for state in obj:
    for chamber in ["upper", "lower"]:
        inf = obj[state][chamber]

        r, d, o = 0, 0, 0
        for typ in inf:
            if typ == "R":
                r += 1
            elif typ == "D":
                d += 1
            else:
                o += 1

        if r > 0:
            ret["%s-%s" % (state, chamber)].append({
                "name": "R",
                "count": r
            })

        if d > 0:
            ret["%s-%s" % (state, chamber)].append({
                "name": "D",
                "count": d
            })

        if o > 0:
            ret["%s-%s" % (state, chamber)].append({
                "name": "I",
                "count": o
            })

print json.dumps(ret)
