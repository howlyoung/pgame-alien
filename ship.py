import pygame


class Ship():

    def __init__(self, screen, shipSetting):
        self.screen = screen
        self.setting = shipSetting

        self.image = pygame.image.load('Valkyrie.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.center = float(self.rect.centerx)
        self.bullets = []

        self.move_right = False
        self.move_left = False

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

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.move_right and self.rect.right < self.screen_rect.right:
            self.center += self.setting.speed_factor
        if self.move_left and self.rect.left > 0:
            self.center -= self.setting.speed_factor

        self.rect.centerx = self.center

    def getCenterx(self):
        return self.rect.centerx

    def getTop(self):
        return self.rect.top

    # 发射子弹
    def shoot_bullet(self):
        self.get_current_bullet().shoot_bullet()

    # 切换子弹
    def change_bullet(self):
        if len(self.bullets) > 1:
            self.bullets[-1], self.bullets[0] = (
                self.bullets[0], self.bullets[1])
