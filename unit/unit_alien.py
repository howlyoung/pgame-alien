from unit.unit import Unit


class UnitAlien(Unit):

    def __init__(self, setting):
        super().__init__(setting)
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.width = self.rect.width

        self.x = float(self.rect.x)
        self.move_flag = 0

    def update(self):
        if self.move_flag >= self.setting.move_interval:
            self.rect.y += 1
            self.move_flag = 0
        else:
            self.move_flag += 1

    def set_poisition(self, poisition):
        self.rect.x = poisition['x']

    def is_hit(self, bulletsprites):
        # 判断是否自己发出的子弹
        if self != bulletsprites.get_shooter():
            self.exist_flag = False
