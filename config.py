import json


class Config():

    def __init__(self):
        pass

    def load_config(self, configpath):
        with open(configpath) as configfile:
            s = configfile.read().rstrip()
            config = json.loads(s)
        self.config = config
        return config

    def get_background(self):
        return tuple(self.config['globals']['background'])

    def get_unit_list(self):
        return self.config['unit']
