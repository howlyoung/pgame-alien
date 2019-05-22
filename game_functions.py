import sys
import pygame


def check_events(ship, ai_settings, screen, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship, ai_settings, bullets, screen)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.move_right = False
    elif event.key == pygame.K_LEFT:
        ship.move_left = False


def check_keydown_events(event, ship, ai_settings, bullets, screen):
    if event.key == pygame.K_q:
        sys.exit()
    elif event.key == pygame.K_RIGHT:
        ship.move_right = True
    elif event.key == pygame.K_LEFT:
        ship.move_left = True
    elif event.key == pygame.K_SPACE:
        ship.shoot_bullet(bullets)


def update_screen(ai_settings, screen, ship, aliens, bullets):
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    # alien.blitme()
    for alien in aliens.sprites():
        alien.blitme()
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    pygame.display.flip()


def update_bullets(bullets, aliens):
    # 如果有碰撞，则字典里会包含碰撞的两个矩形
    collisions = pygame.sprite.groupcollide(bullets, aliens, False, True)
    if collisions:
        for bullet, alien in collisions.items():
            bullet.hidden_bullet()
