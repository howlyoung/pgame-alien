from unit.unit import Unit


class UnitShip(Unit):

    def __init__(self, setting):
        super().__init__(setting)
        self.left = 0
        self.right = 0

        self.move_right = False
        self.move_left = False

    def update(self):
        if self.move_right and self.rect.right < self.right:
            self.center += self.setting.speed_factor
        if self.move_left and self.rect.left > 0:
            self.center -= self.setting.speed_factor

        self.rect.centerx = self.center

    def set_poisition(self, poisition):
        self.rect.centerx = poisition['centerx']
        self.rect.bottom = poisition['bottom']
        self.center = float(self.rect.centerx)

    def set_boundary(self, bound):
        self.left = bound['left']
        self.right = bound['right']
