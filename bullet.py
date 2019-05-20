import pygame

from pygame.sprite import Sprite
from pygame.sprite import Group

class Bullet(Sprite):

    def __init__(self,ai_settings,screen,ship):
        super().__init__()
        self.screen = screen
        self.show_flag = False

        self.rect = pygame.Rect(0,0,ai_settings.bullet_width,ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        if self.show_flag:
            self.y -= self.speed_factor
            self.rect.y = self.y
            if self.rect.bottom <= 0:
                self.show_flag = False 


    def draw_bullet(self):
        pygame.draw.rect(self.screen,self.color,self.rect)


    #生成子弹数组，预生成一定数量的子弹，子弹对象重复利用，不消除
    @staticmethod
    def getBullets(setting,screen,ship):
        bullets = Group()
        limit = 3
        while limit > 0:
            bullet = Bullet(setting,screen,ship)
            bullets.add(bullet)
            limit -= 1

        return bullets