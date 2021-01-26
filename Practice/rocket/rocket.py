import pygame

class Rocket():
    def __init__(self, r_settings, screen):
        self.screen = screen
        self.r_settings = r_settings

        self.image = pygame.image.load("images/rocket.png")
        self.rocket_rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rocket_rect.centerx = self.screen_rect.centerx
        self.rocket_rect.bottom = self.screen_rect.bottom

        self.moving_right = False
        self.moving_left = False
        self.moving_top = False
        self.moving_bottom = False

    def huizhi(self):
        self.screen.blit(self.image, self.rocket_rect)

    def update(self):
        if self.moving_right and self.rocket_rect.right < self.screen_rect.right:
            self.rocket_rect.centerx += self.r_settings.rocket_speed_factor
        if self.moving_left and self.rocket_rect.left > 0:
            self.rocket_rect.centerx -= self.r_settings.rocket_speed_factor
        if self.moving_top and self.rocket_rect.top >0:
            self.rocket_rect.bottom -= self.r_settings.rocket_speed_factor
        if self.moving_bottom and self.rocket_rect.bottom < self.screen_rect.bottom:
            self.rocket_rect.bottom += self.r_settings.rocket_speed_factor


        # self.rect = self.image.get_rect()
        # self.screen_rect = screen.get_rect()
        #
        # self.rect.centerx = self.screen_rect.centerx
        # self.rect.bottom = self.screen_rect.bottom
        # self.center = float(self.rect.centerx)
        #
        # self.moving_right = False
        # self.moving_left = False