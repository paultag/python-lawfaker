

patterns = [
    "Mc",
    "Mac"
]

def normaize_last_name(name):
    name = name.lower()
    name = "%s%s" % (name[0].upper(), name[1:])
    for pattern in patterns:
        if name.startswith(pattern):
            name = "%s%s%s" % (name[:len(pattern)],
                               name[len(pattern)].upper(),
                               name[len(pattern) + 1:])
    return name
