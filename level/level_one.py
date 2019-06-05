from level.level import Level
from unit.unit import Unit
from bullet.bullet_double import BulletDouble
from bullet.bullet_normal import BulletNormal
from setting import Setting


class LevelOne(Level):

    def __init__(self):
        super().__init__()
        self.unit_current_count = 6
        self.unit_exist_count = 0
        self.setting = Setting()

    def load(self, config):
        super().load(config)
        rect = self.screen.get_rect()
        self.ship.set_poisition(
            {'centerx': rect.centerx, 'bottom': rect.bottom})
        self.ship.set_boundary({'left': 0, 'right': rect.right})
        for unit_type, unit_count in self.unit_type_list.items():
            self._create_unit(unit_type, self.unit_current_count)
            self.unit_exist_count += self.unit_current_count
        b = BulletDouble(self.setting.bulletSetting())
        b1 = BulletNormal(self.setting.bulletSetting())
        self.ship.add_bullet(b)
        self.ship.add_bullet(b1)

    def run(self):
        if len(self.unit_list) <= 0:
            self.end()
        if len(self.unit_list) < self.unit_current_count:
            for unit_type, unit_count in self.unit_type_list.items():
                if self.unit_exist_count < unit_count:
                    self._create_unit(unit_type, 1)
                    self.unit_exist_count += 1
        super().run()

    def is_end(self):
        if len(self.unit_list) <= 0:
            return True
        return False

    def end(self):
        print('win')
        self.unit_list.empty()

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
            self.unit_list.add(alien)
