from lawfaker.utils import normaize_last_name


def test_basics():
    names = {
        "MCCRUFT": "McCruft",
        "MACCRUFT": "MacCruft",
        "SMITH": "Smith"
    }
    for name in names:
        got = normaize_last_name(name)
        print got, names[name]
        assert got == names[name]
