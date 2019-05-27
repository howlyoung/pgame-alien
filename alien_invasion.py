import pygame
from setting import Setting
from unit.unit import Unit
from level.level_one import LevelOne
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
    rect = screen.get_rect()
    ship.set_poisition({'centerx': rect.centerx, 'bottom': rect.bottom})
    ship.set_boundary({'left': 0, 'right': rect.right})
    bullets = Bullet.get_overall_sprites()
    level = LevelOne()
    level.load()
    aliens = level.group
    b = BulletDouble(ai_settings.bulletSetting())
    b1 = BulletNormal(ai_settings.bulletSetting())
    ship.add_bullet(b)
    ship.add_bullet(b1)

    while True:
        gf.check_events(ship, ai_settings, screen, bullets)
        ship.update()
        bullets.update()
        aliens.update()
        gf.update_bullets(bullets, aliens)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)
        level.run()


run_game()
