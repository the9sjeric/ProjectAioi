import pygame
import sys

from rocket_settings import Settings
from rocket import Rocketa
import rocket_function as rf

def run_rocket():
    pygame.init()
    r_settings = Settings()
    screen = pygame.display.set_mode(size=(r_settings.screenwidth, r_settings.screenheight))
    pygame.display.set_caption("My Rocket!")

    rocket = Rocket(r_settings, screen)

    while True:
        rf.check_event(rocket)
        rocket.update()
        rf.update_screen(r_settings, screen, rocket)

run_rocket()