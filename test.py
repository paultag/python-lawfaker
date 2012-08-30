#!/usr/bin/env python

from lawfaker.models.legislator import Legislator

test = Legislator()

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
