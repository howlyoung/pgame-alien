import collections

# 各个配置的元组
AlienSetting = collections.namedtuple(
    'AlienSetting', ['move_interval', 'image'])
ShipSetting = collections.namedtuple('ShipSetting', ['speed_factor', 'image'])
BulletSetting = collections.namedtuple(
    'BulletSetting',
    ['speed_factor', 'width', 'height', 'allow', 'color', 'damage'])


class Setting():

    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        self.ship_speed_factor = 1.5

        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allow = 3
        self.damage = 0
        # 毫秒
        self.alien_move_interval = 80

    def alienSetting(self):
        return AlienSetting(self.alien_move_interval, 'resources/Alien.png')

    def shipSetting(self):
        return ShipSetting(self.ship_speed_factor, 'resources/Valkyrie.png')

    def bulletSetting(self):
        return BulletSetting(self.bullet_speed_factor,
                             self.bullet_width, self.bullet_height,
                             self.bullets_allow, self.bullet_color,
                             self.damage)
