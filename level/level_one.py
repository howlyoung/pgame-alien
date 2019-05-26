from level.level import Level
from pygame.sprite import Group


class LevelOne(Level):

    def __init__(self):
        super().__init__()
        # 单元的列表，键位单元类型，值为单元的数量
        self.unit_type_list = {'alien': 10}
        # 单元的精灵组，可以考虑做成类变量，应该定义在基类
        self.unit_list = Group()

    def load(self):
        pass

    def run(self):
        pass

    def end(self):
        pass
