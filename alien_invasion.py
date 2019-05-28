import pygame
from setting import Setting
from unit.unit import Unit
from level.level_one import LevelOne
from level.level_manager import LevelManager
import game_functions as gf
from bullet.bullet import Bullet
from bullet.bullet_double import BulletDouble
from bullet.bullet_normal import BulletNormal


def run_game():
    pygame.init()
    ai_settings = Setting()
    gf.register_unit()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    ship = Unit.create_unit('Ship')
    level_manager = LevelManager(ship, screen)
    bullets = Bullet.get_overall_sprites()

    b = BulletDouble(ai_settings.bulletSetting())
    b1 = BulletNormal(ai_settings.bulletSetting())
    ship.add_bullet(b)
    ship.add_bullet(b1)

    while True:
        level_manager.load()
        aliens = level_manager.level.group
        while level_manager.is_end is False:
            gf.check_events(ship, ai_settings, screen, bullets)
            ship.update()
            bullets.update()
            aliens.update()
            gf.update_bullets(bullets, aliens)
            gf.update_screen(ai_settings, screen, ship, aliens, bullets)
            level_manager.run()


run_game()
