import os
import importlib


def load_modules(__file__, __package__):
    modules = {}
    for file_name in os.listdir(os.path.dirname(__file__)):
        model_name, ext = os.path.splitext(file_name)
        if ext != ".py" or model_name == "__init__":
            continue

        module = importlib.import_module("." + model_name, __package__)
        for name in module.__dict__:
            if name.startswith("__") and name.endswith("__"):
                continue
            modules[name.lower()] = module.__dict__[name]
    return modules
