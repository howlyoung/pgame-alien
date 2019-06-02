from pygame.sprite import Group
# from bullet.bullet import Bullet
import game_functions as gf
import importlib
import pygame


class Level():

    def __init__(self):
        # 单元的列表，键位单元类型，值为单元的数量
        self.unit_type_list = {}
        # 单元的精灵组，可以考虑做成类变量，应该定义在基类
        self.unit_list = Group()
        # self.bullet_sprites = Bullet.get_overall_sprites()
        self.bullet_sprites = Group()

    def set_ship(self, ship):
        self.ship = ship
        self.unit_list.add(ship)

    def set_screen(self, screen):
        self.screen = screen

    # 加载关卡，根据设计好的关卡内容生成单元等
    def load(self):
        # 清空子弹列表
        self.bullet_sprites.empty()

    # 运行关卡
    def run(self):
        gf.check_events(self.ship, self.bullet_sprites)
        self.unit_list.update()
        self.bullet_sprites.update()
        gf.update_bullets(self.bullet_sprites, self.unit_list)
        self.__render()

    def __render(self):
        self.screen.fill((230, 230, 230))
        for unit in self.unit_list:
            unit.blitme(self.screen)
        for bullet in self.bullet_sprites:
            bullet.draw_bullet(self.screen)
        pygame.display.flip()

    def is_end(self):
        pass

    # 结束关卡
    def end(self):
        pass

    @classmethod
    def create_level(cls, name):
        module_name = 'level.level_' + name.lower()
        module = importlib.import_module(module_name)
        className = 'Level' + name
        cls = getattr(module, className)
        return cls()
