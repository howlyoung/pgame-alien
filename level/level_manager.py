from level.level import Level


class LevelManager():

    def __init__(self, ship, screen):
        # 关卡列表
        self.level_list = ['One', 'Two']
        # 当前关卡在列表中的索引
        self.level_index = 0
        self.ship = ship
        self.screen = screen
        self.is_end = False

    def load(self):
        self.is_end = False
        level_name = self.level_list[self.level_index]
        self.level = Level.create_level(level_name)
        self.level.set_ship(self.ship)
        self.level.set_screen(self.screen)
        self.level.load()

    def run(self):
        self.level.run()
        self.end()

    def end(self):
        if self.level.is_end():
            self.level.end()
            self.is_end = True
            self.level_index += 1
