

# 子弹类的基类
class Bullet():

    def __init__(self, owner):
        # 伤害量
        self.damage = 0
        # 子弹精灵列表
        self.sprites = []
        # 发射子弹的对象
        self.owner = owner

    def shoot_bullet(self):
        pass

    def hit_target(self):
        pass

    def update_spriet_track(self, bulletSprite):
        pass

    def getCenterx(self):
        pass

    def getTop(self):
        pass
