import os
from collections.abc import MutableMapping


class FileManager(MutableMapping):
    def __init__(self, path, mode, depth=0):
        self.path = path
        self.files = {}
        self.contents = {}
        for name in os.listdir(path):
            full_path = os.path.join(path, name)
            if os.path.isfile(full_path):
                self.files[name] = open(full_path, mode)
            else:
                if depth > 0:
                    self.files[name] = FileManager(full_path, mode, depth - 1)

    def close_all(self):
        for name in self.keys():
            self.close(name)

    def close(self, name):
        self[name].close()

    def read_all(self):
        for name in self.keys():
            self.read(name)

    def read(self, name):
        self.contents[name] = self[name].read()

    def __getitem__(self, name):
        return self.files[name]

    def __setitem__(self, name, value):
        raise NotImplementedError()

    def __delitem__(self, name):
        full_path = os.path.join(self.path, name)
        os.remove(full_path)
        self.files.__delitem__(name)

    def __iter__(self):
        return self.files.__iter__()

    def __len__(self):
        return self.files.__len__()
