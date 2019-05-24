from bullet.bullet import Bullet
from bullet.bullet_sprite import BulletSprite
import collections


BulletNormalSetting = collections.namedtuple(
    'BulletNormalSetting',
    ['speed_factor', 'width', 'height', 'color'])


class BulletDouble(Bullet):

    def __init__(self, setting):
        super().__init__(setting)

    # 生成子弹精灵，将精灵加入子弹列表，返回子弹精灵，以便后续将其加入全局的精灵组
    def shoot_bullet(self):
        index = self._get_limit()
        if index < self.allow:
            count = 2
            while count > 0:
                bs = BulletSprite(self.setting, self)
                bs.index = index
                bs.bullet_index += 1
                self.sprites.append(bs)
                self.add_overall_sprites(bs)
                if count == 1:
                    bs.rect.centerx += 5
                count -= 1

    # 获取发射限制
    def _get_limit(self):
        tmp = []
        for sprite in self.sprites:
            if sprite.index not in tmp:
                tmp.append(sprite.index)
        return len(tmp)

    def update_spriet_track(self, bulletSprite):
        if bulletSprite in self.sprites:
            if bulletSprite.out_side():
                self.remove_overall_sprites(bulletSprite)
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
