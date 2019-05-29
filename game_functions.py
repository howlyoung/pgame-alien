import sys
import pygame
from pygame.sprite import Group
from unit.unit import Unit
from unit.unit_alien import UnitAlien
from unit.unit_ship import UnitShip
from setting import Setting


def check_events(ship):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.move_right = False
    elif event.key == pygame.K_LEFT:
        ship.move_left = False


def check_keydown_events(event, ship):
    if event.key == pygame.K_q:
        sys.exit()
    elif event.key == pygame.K_RIGHT:
        ship.move_right = True
    elif event.key == pygame.K_LEFT:
        ship.move_left = True
    elif event.key == pygame.K_SPACE:
        ship.shoot_bullet()
    elif event.key == pygame.K_r:
        ship.change_bullet()


def update_screen(ai_settings, screen, ship, aliens, bullets):
    screen.fill(ai_settings.bg_color)
    ship.blitme(screen)
    # alien.blitme()
    for alien in aliens.sprites():
        alien.blitme(screen)
    for bullet in bullets.sprites():
        bullet.draw_bullet(screen)
    pygame.display.flip()


def update_bullets(bullets, aliens):
    # 如果有碰撞，则字典里会包含碰撞的两个矩形
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collisions:
        for bullet, alien in collisions.items():
            bullet.hit_target()


def alien_list(setting):
        aliens = Group()
        sapcing = 30
        tmp = 0
        count = 6
        while(count > 0):
            alien = Unit.create_unit('Alien')
            aliens.add(alien)
            alien.rect.x += tmp
            tmp = alien.rect.x + alien.width + sapcing
            count -= 1
        return aliens


# 注册unit的配置文件，需要改进
def register_unit():
    setting = Setting()
    UnitShip.add_unit(setting.shipSetting())
    UnitAlien.add_unit(setting.alienSetting())
