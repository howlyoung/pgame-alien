import sys
import os


class Base():

    config = {}

    def __init__(self):
        pass

    def get_module_name(self):
        mod = sys.modules['__main__']
        file = getattr(mod, '__file__', None)
        return file and os.path.splitext(os.path.basename(file))[0]

    def get_config(self):
        classname = self.__class__.__name__
        if classname in self.config:
            return self.config[classname]
        else:
            return None

    @classmethod
    def init_config(cls, config):
        cls.config = config
