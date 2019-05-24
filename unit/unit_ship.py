from unit.unit import Unit


class UnitShip(Unit):

    def __init__(self, screen, setting):
        super().__init__(screen, setting)

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.center = float(self.rect.centerx)

        self.move_right = False
        self.move_left = False

    def update(self):
        if self.move_right and self.rect.right < self.screen_rect.right:
            self.center += self.setting.speed_factor
        if self.move_left and self.rect.left > 0:
            self.center -= self.setting.speed_factor

        self.rect.centerx = self.center
