from torch.utils.data import DataLoader
from torchvision.datasets import cifar


class CIFAR10:
    def __init__(self, args):
        super(CIFAR10, self).__init__()

        if args.train_dir is not None:
            pass

        self.train_set = cifar.CIFAR10(args.train_dir or args.data_dir, train=True, download=True)
        self.val_set = cifar.CIFAR10(args.val_dir or args.data_dir, train=False, download=True)

        self.train_loader = DataLoader(self.train_set,
                                       batch_size=args.batch_size if args.train_batch_size is None else args.train_batch_size)
