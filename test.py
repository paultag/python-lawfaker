#!/usr/bin/env python

from lawfaker.populator import run_populator

populators = [
    "lawfaker.populators.core.first_name",
    "lawfaker.populators.core.last_name",
    "lawfaker.populators.core.middle_name",
    "lawfaker.populators.core.title",
    "lawfaker.populators.usa.state",
    "lawfaker.populators.usa.chamber",
    "lawfaker.populators.usa.party"
]

class Person(object):
    pass

test = Person()
for populator in populators:
    run_populator(populator, test)

print "%s %s %s %s" % (
    test.title,
    test.first_name,
    "%s." % (test.middle_name[0]),
    test.last_name
)

print "  %s memeber of the %s from %s, %s" % (
    {
        "R": "Republican",
        "D": "Democrat",
        "I": "Independent"
    }[test.party],
    {
        "lower": "House",
        "upper": "Senate"
    }[test.chamber],
    test.state.capital,
    test.state,
)
