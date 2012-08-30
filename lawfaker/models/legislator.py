from lawfaker.populator import run_populators
from lawfaker.models.person import Person

populators = [
    "lawfaker.populators.usa.state",
    "lawfaker.populators.usa.chamber",
    "lawfaker.populators.usa.party"
]

class Legislator(Person):
    def __init__(self):
        self = run_populators(populators, self)
