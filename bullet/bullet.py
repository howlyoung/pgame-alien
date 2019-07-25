from pygame.sprite import Group
from base.base import Base


# 子弹类的基类
class Bullet(Base):

    # 存放所有的子弹精灵，用于碰撞等检测
    overall_sprites = Group()
    # 标识
    flag = ''

    def __init__(self):
        # 伤害量
        super().__init__()
        # 基类处获取配置
        setting = self.get_config()
        self.damage = 0
        # 子弹精灵列表
        self.sprites = []
        # 子弹数量
        self.allow = setting['allow']
        # 伤害量
        self.damage = setting['damage']
        # 子弹速度
        self.speed_factor = setting['speed_factor']
        # 子弹宽度
        self.width = setting['width']
        # 子弹高度
        self.height = setting['height']
        # 子弹颜色
        self.color = setting['color']
        # 保存设置
        self.setting = setting
        # 发射子弹的对象
        self.owner = None

    # 设置子弹的对象
    def set_owner(self, owner):
        if self.owner:
            # 如果已经被设置为其他对象的子弹，则将其从其他对象中清除
            self.owner.remove_bullet(self)
        self.owner = owner
        return True

    # 清除子弹设置
    def clear_owner(self, owner):
        if self.owner and self.owner == owner:
            self.owner = None
            return True
        else:
            return False

    def shoot_bullet(self):
        pass

    def hit_target(self, bulletsprite, target):
        pass

    def update_spriet_track(self, bulletSprite):
        pass

    def getCenterx(self):
        pass

    def getTop(self):
        pass

    @classmethod
    def creaet_by_flag(ctl, flag):
        if ctl.flag == flag:
            pass

    # 获取全局子弹精灵列表
    @classmethod
    def get_overall_sprites(ctl):
        return ctl.overall_sprites

    # 将精灵加入列表
    @classmethod
    def add_overall_sprites(ctl, sprites):
        ctl.overall_sprites.add(sprites)

    @classmethod
    def remove_overall_sprites(ctl, sprites):
        ctl.overall_sprites.remove(sprites)

    @classmethod
    def create_bullet(ctl, setting):
        return ctl(setting)

    @classmethod
    def clear_list(cls):
        cls.overall_sprites.empty()
