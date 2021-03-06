import pygame
from setting import Setting
from unit.unit import Unit
from level.level_manager import LevelManager
import game_functions as gf
from config import Config


def run_game():
    pygame.init()
    ai_settings = Setting()
    gf.register_unit()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    ship = Unit.create_unit('Ship')
    level_manager = LevelManager(ship, screen)
    config = Config()
    config.load_config('config.json')

    while True:
        level_manager.load(config)
        while level_manager.is_end is False:
            level_manager.run()


run_game()
