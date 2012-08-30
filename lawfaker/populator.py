import importlib


def run_populator(populator_path, obj):
    module, func = populator_path.rsplit(".", 1)
    mod = importlib.import_module(module)
    fltr = getattr(mod, func)
    return fltr(obj)


def run_populators(pop_stack, obj):
    for populator in pop_stack:
        obj = run_populator(populator, obj)
    return obj
