#!/usr/bin/env python

from lawfaker.populator import run_populator

populators = [
    "lawfaker.populators.core.first_name",
    "lawfaker.populators.core.last_name",
    "lawfaker.populators.core.middle_name"
]

class Person(object):
    pass

test = Person()

for populator in populators:
    run_populator(populator, test)

print test.first_name
