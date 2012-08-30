#

import random
import json
import os

rand_pool = 100

paths = [
    "%s/data" % (os.path.abspath(".")),
    "%s/../../data" % (os.path.abspath(__file__)),
    "/usr/share/lawfaker/data/",
    "/usr/local/share/lawfaker/data/"
]


def load_data(payload):
    for path in paths:
        fpath = "%s/%s.json" % (path, payload)
        if os.path.exists(fpath):
            return json.load(open(fpath, 'r'))
    return None


def calculate_pcts(objects):
    total = float(0)
    for obj in objects:
        total += int(obj['count'])
    for obj in objects:
        pct = float(obj['count']) / total
        obj['pct'] = pct
    return objects


def get_random_choice(objects, filters=[]):
    # We either have a "pct" attr, or a "count" attr. If we have a "count",
    # then we should calculate pct.
    pool = []

    if filters != []:
        nobj = []
        for filt in filters:
            nobj += objects[filt]
        objects = nobj

    if "count" in objects[0]:
        objects = calculate_pcts(objects)

    for obj in objects:
        pct = obj['pct']
        if isinstance(obj['pct'], basestring):
            if "%" in obj['pct']:
                pct = float(obj['pct'].replace("%", ""))
        if pct > 1:
            pct = pct / 100
        obj['pct'] = pct

        for x in range(0, int(obj['pct'] * 100)):
            pool.append(obj)

    return random.choice(pool)
