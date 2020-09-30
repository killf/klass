from util import load_modules

__ALL__ = ["names", "create"]

modules = load_modules(__file__, __package__)


def names():
    return modules.keys()


def create(args):
    if not args.dataset:
        raise ValueError("The dataset field is required.")

    dataset = args.dataset.lower()
    if dataset not in modules:
        raise ValueError(f"The dataset({dataset}) does not exist.")

    return modules[dataset](args)
