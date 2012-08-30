from lawfaker.data import load_data, get_random_choice
import random
import us


def state(obj):
    sts = load_data("states")
    state = get_random_choice(sts)
    obj.state = us.states.lookup(state['name'])
    if obj.state is None:
        raise Exception(state)

    return obj


def chamber(obj):
    state = obj.state.abbr.lower()
    chamber = get_random_choice(load_data("chambers"), filters=[state])['name']
    obj.chamber = chamber
    return obj


def party(obj):
    state = obj.state.abbr.lower()
    chamber = obj.chamber
    party = get_random_choice(load_data("parties"), filters=["%s-%s" % (
        state, chamber
    )])['name']
    obj.party = party
    return obj
