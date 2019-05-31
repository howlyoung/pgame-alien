import pygame
from pygame.sprite import Sprite
import importlib


class Unit(Sprite):

    # 配置字典
    setting_list = {}

    def __init__(self, setting):
        super().__init__()
        self.setting = setting

        self.image = pygame.image.load(setting.image)
        self.rect = self.image.get_rect()

        self.bullets = []

        self.exist_flag = True

    def set_poisition(self):
        pass

    # 增加新子弹类型
    def add_bullet(self, bullet):
        if bullet.set_owner(self):
            self.bullets.append(bullet)

    # 移除子弹
    def remove_bullet(self, bullet):
        if bullet.clear_owner(self):
            self.bullets.remove(bullet)

    # 获取当前使用子弹
    def get_current_bullet(self):
        return self.bullets[0]

    # 绘制单元
    def blitme(self, screen):
        screen.blit(self.image, self.rect)

    def update(self):
        pass

    def getCenterx(self):
        return self.rect.centerx

    def getTop(self):
        return self.rect.top

    # 发射子弹
    def shoot_bullet(self):
        bullet = self.get_current_bullet()
        if bullet:
            bullet.shoot_bullet()

    # 切换子弹
    def change_bullet(self):
        if len(self.bullets) > 1:
            self.bullets[-1], self.bullets[0] = (
                self.bullets[0], self.bullets[1])

    # 被命中
    def is_hit(self, bulletsprites):
        pass

    # 创建对象，根据名字动态的导入模块，从list中获取已经注册好的配置
    @staticmethod
    def create_unit(name):
        module_name = 'unit.unit_' + name.lower()
        module = importlib.import_module(module_name)
        className = 'Unit' + name
        cls = getattr(module, className)
        return cls(cls.setting_list[cls])

    # 将配置注册到类变量中，创建对象时从list中获取
    @classmethod
    def add_unit(cls, setting):
        cls.setting_list[cls] = setting
