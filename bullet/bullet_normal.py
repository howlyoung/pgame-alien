from bullet.bullet import Bullet
from bullet.bullet_sprite import BulletSprite
import collections


BulletNormalSetting = collections.namedtuple(
    'BulletNormalSetting',
    ['speed_factor', 'width', 'height', 'color'])


# 普通攻击子弹
class BulletNormal(Bullet):

    def __init__(self):
        super().__init__()

    # 生成子弹精灵，将精灵加入子弹列表，返回子弹精灵，以便后续将其加入全局的精灵组
    def shoot_bullet(self):
        if len(self.sprites) < self.allow:
            bs = BulletSprite(self.setting, self)
            self.sprites.append(bs)
            # self.add_overall_sprites(bs)
            return bs

    def update_spriet_track(self, bulletSprite):
        if bulletSprite in self.sprites:
            if bulletSprite.out_side():
                # self.remove_overall_sprites(bulletSprite)
                bulletSprite.destroy()
                self.sprites.remove(bulletSprite)
            else:
                position = bulletSprite.get_position()
                position['y'] -= 1
                bulletSprite.set_position(position)

    def getCenterx(self):
        return self.owner.getCenterx()

    def getTop(self):
        return self.owner.getTop()

    def hit_target(self, bulletSprite, target):
        if bulletSprite in self.sprites:
            self.sprites.remove(bulletSprite)
            bulletSprite.destroy()
