class DataSet:
    def __init__(self):
        self.train = None
        self.val = None
        self.test = None


def create_data(args):
    if not args.dataset:
        raise ValueError("The dataset field is required.")
    pass
