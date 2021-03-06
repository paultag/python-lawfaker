from lawfaker.data import load_data, get_random_choice
from lawfaker.utils import normaize_last_name
import random


def first_name(obj):
    fnames = load_data("first_names")
    name = get_random_choice(fnames)
    obj.first_name = name['name']
    obj.gender = name['gender']
    return obj


def middle_name(obj):
    fnames = load_data("first_names")
    name = get_random_choice(fnames)
    obj.middle_name = name['name']  # Hack!
    return obj


def last_name(obj):
    lnames = load_data("last_names")
    name = get_random_choice(lnames)['name']
    name = normaize_last_name(name)
    obj.last_name = name
    return obj


def title(obj):
    titles = load_data("titles")
    title = get_random_choice(titles, [obj.gender, "both"])
    obj.title = title['name']
    return obj
