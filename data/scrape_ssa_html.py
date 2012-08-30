#!/usr/bin/env python

from lxml.html import fromstring
import json
import sys

page = fromstring(open(sys.argv[1], 'r').read())
table = page.xpath("//table")[1]

ret = []

for row in table.xpath(".//tr"):
    tds = row.xpath(".//td")
    if len(tds) != 5:
        continue

    tds = [x.text_content() for x in tds]
    rank, male, male_pct, female, female_pct = tds

    ret.append({
        "name": male,
        "gender": "male",
        "pct": male_pct
    })
    ret.append({
        "name": female,
        "gender": "female",
        "pct": female_pct
    })

print json.dumps(ret)
