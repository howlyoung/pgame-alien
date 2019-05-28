from level.level import Level
from unit.unit import Unit
from pygame.sprite import Group
import sys


class LevelOne(Level):

    def __init__(self):
        super().__init__()
        self.unit_type_list = {'Alien': 10}
        self.group = Group()
        self.unit_current_count = 6
        self.unit_exist_count = 0

    def load(self):
        rect = self.screen.get_rect()
        self.ship.set_poisition(
            {'centerx': rect.centerx, 'bottom': rect.bottom})
        self.ship.set_boundary({'left': 0, 'right': rect.right})
        for unit_type, unit_count in self.unit_type_list.items():
            self._create_unit(unit_type, self.unit_current_count)
            self.unit_exist_count += self.unit_current_count

    def run(self):
        if len(self.group) <= 0:
            self.end()
        if len(self.group) < self.unit_current_count:
            for unit_type, unit_count in self.unit_type_list.items():
                if self.unit_exist_count < unit_count:
                    self._create_unit(unit_type, 1)
                    self.unit_exist_count += 1

    def is_end(self):
        if len(self.group) <= 0:
            return True
        return False

    def end(self):
        print('win')
        self.group.empty()

    # 生成单元
    def _create_unit(self, unit_type, count):
        sapcing = 30
        tmp = 0
        x = 0
        while count > tmp:
            alien = Unit.create_unit(unit_type)
            alien.rect.x += x
            x = alien.rect.x + alien.width + sapcing
            tmp += 1
            self.group.add(alien)
