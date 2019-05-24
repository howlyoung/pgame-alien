import pygame
from setting import Setting
from unit.unit_ship import UnitShip
import game_functions as gf
from bullet.bullet import Bullet
from bullet.bullet_double import BulletDouble
from bullet.bullet_normal import BulletNormal


def run_game():
    pygame.init()
    ai_settings = Setting()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    ship = UnitShip(screen, ai_settings.shipSetting())
    bullets = Bullet.get_overall_sprites()
    aliens = gf.alien_list(screen, ai_settings.alienSetting())
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


run_game()
