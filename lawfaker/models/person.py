from lawfaker.populator import run_populators

populators = [
    "lawfaker.populators.core.first_name",
    "lawfaker.populators.core.last_name",
    "lawfaker.populators.core.middle_name",
    "lawfaker.populators.core.title"
]

class Person(object):
    def __init__(self):
        self = run_populators(populators, self)
