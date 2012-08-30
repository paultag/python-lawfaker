#!/usr/bin/env python

from lawfaker.populator import run_populator

populators = [
    "lawfaker.populators.core.first_name",
    "lawfaker.populators.core.last_name",
    "lawfaker.populators.core.middle_name",
    "lawfaker.populators.core.title"
]

class Person(object):
    pass

for x in range(0, 20):
    test = Person()
    for populator in populators:
        run_populator(populator, test)
    print "%s %s %s %s" % (
        test.title,
        test.first_name,
        test.middle_name,
        test.last_name
    )
