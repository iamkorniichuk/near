from collections.abc import MutableMapping
from django.conf import settings


class RestorableSettings(MutableMapping):
    def __init__(self, **kwargs):
        self.previous = {}
        for name, value in kwargs.items():
            self[name] = value

    def restore_all(self):
        for name in self.keys():
            self.restore(name)

    def restore(self, name):
        setattr(settings, name, self[name])

    def __getitem__(self, name):
        return self.previous[name]

    def __setitem__(self, name, value):
        try:
            self.previous[name] = getattr(settings, name)
            setattr(settings, name, value)
        except AttributeError:
            pass

    def __delitem__(self, name):
        self.restore(name)
        self.previous.__delitem__(name)

    def __iter__(self):
        return self.previous.__iter__()

    def __len__(self):
        return self.previous.__len__()
