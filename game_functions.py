import sys
import pygame
from bullet import Bullet
from alien import Alien

def check_events(ship,ai_settings,screen,bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ship,ai_settings,bullets,screen)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)

def check_keyup_events(event,ship):
    if event.key == pygame.K_RIGHT:
        ship.move_right = False
    elif event.key == pygame.K_LEFT:
        ship.move_left = False

def check_keydown_events(event,ship,ai_settings,bullets,screen):
    if event.key == pygame.K_q:
        sys.exit()
    elif event.key == pygame.K_RIGHT:
        ship.move_right = True
    elif event.key == pygame.K_LEFT:
        ship.move_left = True
    elif event.key == pygame.K_SPACE:
        if len(bullets) < ai_settings.bullets_allowed:
            new_bullet = Bullet(ai_settings, screen, ship)
            bullets.add(new_bullet)

def update_screen(ai_settings,screen,ship,aliens,bullets):
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    # alien.blitme()
    for alien in aliens.sprites():
        alien.blitme()
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    pygame.display.flip()

def update_bullets(bullets,aliens):
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
        fit_flag = False
        for alien in aliens.copy():
            if bullet.rect.x > alien.rect.x and bullet.rect.x < (
                    alien.rect.x + alien.width) and bullet.rect.y > alien.rect.y and bullet.rect.y < (
                    alien.rect.y + alien.rect.height):
                # 命中
                aliens.remove(alien)
                fit_flag = True
                break
        if fit_flag == True:
            bullets.remove(bullet)
