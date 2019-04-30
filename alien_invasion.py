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
    ship = Ship(screen,ai_settings)
    bullets = Group()
    alien = Alien(ai_settings,screen)

    while True:
        gf.check_events(ship,ai_settings,screen,bullets)
        ship.update()
        bullets.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings,screen,ship,alien,bullets)

run_game()