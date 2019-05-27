from pygame.sprite import Group


class Level():

    def __init__(self):
        # 单元的列表，键位单元类型，值为单元的数量
        self.unit_type_list = {}
        # 单元的精灵组，可以考虑做成类变量，应该定义在基类
        self.unit_list = Group()

    # 加载关卡，根据设计好的关卡内容生成单元等
    def load(self):
        pass

    # 运行关卡
    def run(self):
        pass

    # 结束关卡
    def end(self):
        pass
