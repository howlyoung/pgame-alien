from level.level import Level


class LevelOne(Level):

    def __init__(self):
        super().__init__()
        self.unit_type_list = {'Alien': 10}

    def load(self):
        count = 5
        for unit_type, unit_count in self.unit_type_list.items():
            if unit_count > count:
                tmp = 0
                while count > tmp:
                    

    def run(self):
        pass

    def end(self):
        pass
