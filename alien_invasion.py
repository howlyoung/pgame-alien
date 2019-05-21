import pygame
from setting import Setting
from ship import Ship
from alien import Alien
from bullet import Bullet
import game_functions as gf


def run_game():
    pygame.init()
    ai_settings = Setting()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    ship = Ship(screen, ai_settings.shipSetting())
    bullets = Bullet.getBullets(ai_settings.bulletSetting(), screen)

    aset = ai_settings.alienSetting()
    aliens = Alien.getAliens(aset, screen)

    while True:
        gf.check_events(ship, ai_settings, screen, bullets)
        ship.update()
        bullets.update()
        aliens.update()
        gf.update_bullets(bullets, aliens)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)


run_game()
