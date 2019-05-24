import pygame
from pygame.sprite import Sprite
from pygame.sprite import Group


class Bullet(Sprite):
    def __init__(self, ai_settings, screen):
        super().__init__()
        self.screen = screen
        # 初始设置为不显示
        self.show_flag = False

        # 生成矩形
        self.rect = pygame.Rect(0, 0, ai_settings.width, ai_settings.height)

        # 设置颜色和速度
        self.color = ai_settings.color
        self.speed_factor = ai_settings.speed_factor

    def update(self):
        if self.show_flag is True:
            self.y -= self.speed_factor
            self.rect.y = self.y
            if self.rect.bottom <= 0:
                self.show_flag = False

    # 发射子弹
    def shoot_bullet(self, ship):
        # 子弹的初始位置为飞船的位置
        if self.show_flag is False:
            self.show_flag = True
            self.rect.centerx = ship.getCenterx()
            self.rect.top = ship.getTop()
            self.y = float(self.rect.y)
            return True
        else:
            return False

    # 子弹消失
    def hidden_bullet(self):
        self.show_flag = False

    # 绘制子弹
    def draw_bullet(self):
        if self.show_flag is True:
            pygame.draw.rect(self.screen, self.color, self.rect)

    # 生成子弹数组，预生成一定数量的子弹，子弹对象重复利用，不消除
    @staticmethod
    def getBullets(setting, screen):
        bullets = Group()
        limit = setting.allowed
        while limit > 0:
            bullet = Bullet(setting, screen)
            bullets.add(bullet)
            limit -= 1
        return bullets
