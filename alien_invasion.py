import sys

import pygame

from setting import Setting
from ship import Ship
from alien import Alien
from pygame.sprite import Group

import game_functions as gf

def run_game():
    pygame.init()
    ai_settings = Setting()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    ship = Ship(screen,ai_settings.shipSetting())
    bullets = Group()
    aliens = Group()
    gf.defend_aliens(aliens,5,ai_settings,screen)
    # alien = Alien(ai_settings,screen)

    while True:
        gf.check_events(ship,ai_settings,screen,bullets)
        ship.update()
        bullets.update()
        aliens.update()
        gf.update_bullets(bullets,aliens)
        gf.update_screen(ai_settings,screen,ship,aliens,bullets)

run_game()