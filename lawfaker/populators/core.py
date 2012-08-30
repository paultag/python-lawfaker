from lawfaker.data import load_data
import random


def first_name(obj):
    fnames = load_data("first_names")
    name = random.choice(fnames)
    obj.first_name = name['name']
    obj.gender = name['gender']
    return obj


def middle_name(obj):
    fnames = load_data("first_names")
    name = random.choice(fnames)
    obj.middle_name = name['name']  # Hack!
    return obj


def last_name(obj):
    lnames = load_data("last_names")
    name = random.choice(lnames)
    obj.last_name = name['name']
    return obj


def title(obj):
    titles = load_data("titles")
    title = random.choice(random.choice([
        titles[obj.gender],
        titles["either"]
    ]))
    obj.title = title
    return obj
