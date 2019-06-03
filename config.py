import json


class Config():

    def __init__(self):
        pass

    def load_config(self, configpath):
        with open(configpath) as configfile:
            s = configfile.read().rstrip()
            config = json.loads(s)
        return config
