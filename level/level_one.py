from level.level import Level
from unit.unit import Unit
from pygame.sprite import Group
import sys


class LevelOne(Level):

    def __init__(self):
        super().__init__()
        self.unit_type_list = {'Alien': 10}
        self.group = Group()

    def load(self):
        count = 6
        sapcing = 30
        for unit_type, unit_count in self.unit_type_list.items():
            if unit_count > count:
                tmp = 0
                x = 0
                while count > tmp:
                    alien = Unit.create_unit(unit_type)
                    alien.rect.x += x
                    x = alien.rect.x + alien.width + sapcing
                    tmp += 1
                    self.group.add(alien)

    def run(self):
        if len(self.group) <= 0:
            self.end()

    def end(self):
        print('win')
        sys.exit()
