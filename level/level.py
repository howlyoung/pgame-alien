from pygame.sprite import Group
import importlib


class Level():

    def __init__(self):
        # 单元的列表，键位单元类型，值为单元的数量
        self.unit_type_list = {}
        # 单元的精灵组，可以考虑做成类变量，应该定义在基类
        self.unit_list = Group()

    def set_ship(self, ship):
        self.ship = ship

    def set_screen(self, screen):
        self.screen = screen

    # 加载关卡，根据设计好的关卡内容生成单元等
    def load(self):
        pass

    # 运行关卡
    def run(self):
        pass

    def is_end(self):
        pass

    # 结束关卡
    def end(self):
        pass

    @classmethod
    def create_level(cls, name):
        module_name = 'level.level_' + name.lower()
        module = importlib.import_module(module_name)
        className = 'Level' + name
        cls = getattr(module, className)
        return cls()
