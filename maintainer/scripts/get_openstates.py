#!/usr/bin/env python

from sunlight import openstates
import json

states = openstates.all_metadata()

ret = {}

for state in states:
    abbr = state['abbreviation']
    ret[abbr] = {
        "upper": [],
        "lower": []
    }
    legislators = openstates.legislators(state=abbr)
    for leg in legislators:
        if "chamber" not in leg:
            continue  # Dewhurst.

        chamber = leg['chamber']
        party = leg['party']
        ret[abbr][chamber].append(party[0])

open("openstates.json", 'w').write(json.dumps(ret))
