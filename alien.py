#1
import pygame
from pygame.sprite import Sprite
from pygame.sprite import Group

class Alien(Sprite):

    def __init__(self,AlienSetting,screen):
        super().__init__()
        self.screen = screen
        #self.ai_settings = ai_settings
        self.setting = AlienSetting

        self.image = pygame.image.load('Alien.png')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.width = self.rect.width

        self.x = float(self.rect.x)
        self.move_flag = 0

    def blitme(self):
        self.screen.blit(self.image,self.rect)

    def update(self):
        if self.move_flag >= self.setting.move_interval:
            self.rect.y += 1
            self.move_flag = 0
        else:
            self.move_flag += 1


    @classmethod
    def getAliens(cls,setting,screen):
        aliens = Group()
        sapcing = 30
        tmp = 0
        count = 6
        while(count > 0):
            alien = Alien(setting,screen)
            aliens.add(alien)
            alien.rect.x += tmp
            tmp = alien.rect.x + alien.width + sapcing
            count -= 1
        return aliens

