import importlib

def run_populator(populator_path, obj):
    module, func = populator_path.rsplit(".", 1)
    mod = importlib.import_module(module)
    fltr = getattr(mod, func)
    return run_populator(fltr, obj)
