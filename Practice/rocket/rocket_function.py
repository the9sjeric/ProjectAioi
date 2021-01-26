import sys
import pygame

def check_event(rocket):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, rocket)

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, rocket)

def check_keydown_events(event, rocket):
    """响应按键"""
    if event.key == pygame.K_RIGHT:
        rocket.moving_right = True
    elif event.key == pygame.K_LEFT:
        rocket.moving_left = True
    elif event.key == pygame.K_UP:
        rocket.moving_top = True
    elif event.key == pygame.K_DOWN:
        rocket.moving_bottom = True

def check_keyup_events(event, rocket):
    if event.key == pygame.K_RIGHT:
        rocket.moving_right = False
    elif event.key == pygame.K_LEFT:
        rocket.moving_left = False
    elif event.key == pygame.K_UP:
        rocket.moving_top = False
    elif event.key == pygame.K_DOWN:
        rocket.moving_bottom = False

def update_screen(r_settings, screen , rocket):
    screen.fill(r_settings.bg_color)
    rocket.huizhi()

    pygame.display.flip()
