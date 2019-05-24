import pygame
from pygame.sprite import Sprite


class Unit(Sprite):

    def __init__(self, screen, setting):
        super().__init__()
        self.screen = screen
        self.setting = setting

        self.image = pygame.image.load(setting.image)
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.bullets = []

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
    def blitme(self):
        self.screen.blit(self.image, self.rect)

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
