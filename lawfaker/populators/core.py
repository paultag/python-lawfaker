from lawfaker.data import load_data

def first_name(obj):
    fnames = load_data("first_names")
    print fnames
    return obj

last_name = first_name
middle_name = first_name
