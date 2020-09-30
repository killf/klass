import os

__all__ = ["CIFAR10"]


class CIFAR10:
    def __init__(self, args):
        super(CIFAR10, self).__init__()

        from torch.utils.data import DataLoader
        from torchvision.datasets import cifar

        default_root = os.path.join(os.path.expanduser('~'), ".klass/data/cifar10")
        self.train_set = cifar.CIFAR10(args.get("train_dir", "data_dir", default_root), train=True, download=True)
        self.val_set = cifar.CIFAR10(args.get("val_dir", "data_dir", default_root), train=False, download=True)
        self.test_set = cifar.CIFAR10(args.get("test_dir", "data_dir", default_root), train=False, download=True)

        self.train_loader = DataLoader(self.train_set, batch_size=args.get("train_batch_size", "batch_size", 1))
        self.val_loader = DataLoader(self.val_set, batch_size=args.get("val_batch_size", "batch_size", 1))
        self.test_loader = DataLoader(self.test_set, batch_size=args.get("test_batch_size", "batch_size", 1))

    def __repr__(self):
        return self.__class__.__name__
