import pygame
from pygame.sprite import Sprite


class BulletSprite(Sprite):
    def __init__(self, ai_settings, bullet):
        super().__init__()
        # 生成矩形
        self.rect = pygame.Rect(0, 0, ai_settings.width, ai_settings.height)
        # 伤害量
        self.damage = 0
        # 指向子弹对象
        self.bullet = bullet

        # 设置颜色和速度
        self.color = ai_settings.color
        self.speed_factor = ai_settings.speed_factor

        self.rect.centerx = self.bullet.getCenterx()
        self.rect.top = self.bullet.getTop()
        # 标记是第几发子弹
        self.index = 0
        # 如果子弹是多发的，标记是其中的第几发
        self.bullet_index = 0
        # 是否存在于碰撞列表
        self.exist_flag = True

    def update(self):
        # 具体的轨迹计算，由子弹类提供算法
        self.bullet.update_spriet_track(self)

    # 绘制子弹
    def draw_bullet(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

    # 返回精灵位置
    def get_position(self):
        return {'x': self.rect.left,
                'y': self.rect.y, 'centerx': self.rect.centerx}

    # 设置位置
    def set_position(self, position):
        if "y" in position:
            self.rect.y = position['y']
        if "x" in position:
            self.rect.x = position['x']
        if "centerx" in position:
            self.rect.centerx = position['centerx']

    # 是否出界
    def out_side(self):
        if self.rect.bottom <= 0:
            return True
        else:
            return False

    # 命中目标的处理
    def hit_target(self, target):
        self.bullet.hit_target(self, target)

    # 子弹消失
    def destroy(self):
        self.exist_flag = False

    # 获取发射子弹的对象
    def get_shooter(self):
        return self.bullet.owner
