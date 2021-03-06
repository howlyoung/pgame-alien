from pygame.sprite import Group
from base.base import Base
from pygame.sprite import Sprite
import importlib
import pygame


# 子弹类的基类
class Bullet(Base, Sprite):

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
        # 初始位置坐标
        self.poisition = []
        # 生成矩形
        self.rect = pygame.Rect(
            0, 0, setting['width'], setting['height'])

    # 设置子弹的对象
    def set_owner(self, owner):
        self.owner = owner
        return True

    # 设置位置
    def set_poisition(self, poisition):
        self.poisition = poisition

    # 设置位置
    def get_poisition(self, poisition):
        return self.poisition

    # 更新子弹位置
    def update(self):
        pass

    def hit_target(self, bulletsprite, target):
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
    def create_bullet(ctl, modulename, classname):
        module = importlib.import_module(modulename)
        cls = getattr(module, classname)
        return cls()

    @classmethod
    def clear_list(cls):
        cls.overall_sprites.empty()
