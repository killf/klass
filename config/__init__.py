import json
import os


class Config(dict):
    def __getattr__(self, key):
        return self.__getitem__(key) if key in self.keys() else None

    def __setattr__(self, key, value):
        return self.__setitem__(key, value)

    def get(self, key, default_key=None, default_value=None):
        result = self.__getattr__(key)
        if result is not None:
            return result

        if default_key is not None:
            result = self.__getattr__(default_key)
        if result is not None:
            return result

        if default_value is not None:
            return default_value


def config(item):
    if isinstance(item, dict):
        return Config({k: config(v) for k, v in item.items()})
    elif isinstance(item, list):
        return list(config(v) for v in item)
    elif isinstance(item, tuple):
        return tuple(config(v) for v in item)
    else:
        return item


def load_config(file) -> Config:
    if not file.endswith(".json"):
        file = file + ".json"

    if not os.path.isabs(file):
        folder = os.path.dirname(__file__)
        file = os.path.join(folder, file)

    if not os.path.exists(file):
        raise FileNotFoundError(file)

    return config(json.load(open(file, "r", encoding="utf8")))
