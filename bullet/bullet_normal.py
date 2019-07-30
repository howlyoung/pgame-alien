from bullet.bullet import Bullet
import collections


BulletNormalSetting = collections.namedtuple(
    'BulletNormalSetting',
    ['speed_factor', 'width', 'height', 'color'])


# 普通攻击子弹
class BulletNormal(Bullet):

    def __init__(self):
        super().__init__()

    def update(self):
        self.poisition['y'] -= 1

    def hit_target(self, target):
        pass
