from bullet.bullet import Bullet
from bullet.bullet_sprite import BulletSprite
import collections


BulletNormalSetting = collections.namedtuple(
    'BulletNormalSetting',
    ['speed_factor', 'width', 'height', 'color'])


# 普通攻击子弹
class BulletNormal(Bullet):

    def __init__(self, owner):
        super().__init__(owner)
        # 可发射子弹数量
        self.allow = 3
        self.speed_factor = 1
        self.width = 3
        self.height = 15
        self.color = (60, 60, 60)
        self.setting = BulletNormalSetting(
            self.speed_factor, self.width, self.height, self.color)

    # 生成子弹精灵，将精灵加入子弹列表，返回子弹精灵，以便后续将其加入全局的精灵组
    def shoot_bullet(self):
        if len(self.sprites) < self.allow:
            bs = BulletSprite(self.setting, self)
            self.sprites.append(bs)
            return bs

    def update_spriet_track(self, bulletSprite):
        if bulletSprite in self.sprites:
            if bulletSprite.out_side():
                # 退出精灵组 可改进
                bulletSprite.kill()
                self.sprites.remove(bulletSprite)
            else:
                position = bulletSprite.get_position()
                position['y'] -= 1
                bulletSprite.set_position(position)

    def getCenterx(self):
        return self.owner.getCenterx()

    def getTop(self):
        return self.owner.getTop()

    def hit_target(self, bulletSprite):
        if bulletSprite in self.sprites:
            self.sprites.remove(bulletSprite)
