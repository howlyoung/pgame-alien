import os
import json


class Config():

    def __init__(self):
        self.config = {}

    def load_config(self, configpath, prefix=''):
        if os.path.isdir(configpath):
            filelist = os.listdir(configpath)
            if prefix == '':
                nextprefix = configpath
            else:
                nextprefix = prefix + "." + configpath
            for filepath in filelist:
                path = configpath + "/" + filepath
                self.load_config(path, nextprefix)
        else:
            with open(configpath) as configfile:
                s = configfile.read().rstrip()
                config = json.loads(s)
            if prefix == '':
                index = os.path.basename(configpath)
            else:
                # index = prefix + "." + os.path.basename(configpath)
                index = os.path.basename(configpath)

            self.config[index] = config

if __name__ == '__main__':
    config = Config()
    config.load_config('test')
    print(config.config)
