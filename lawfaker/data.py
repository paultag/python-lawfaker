#

import json
import os


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
