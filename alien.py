import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """A class to represent a single Alien in the fleet."""

    def __init__(self, ai_settings, screen):
        """initialize Alien and set its starting position."""
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # load the image and set its rect attribute.
        self.image = pygame.image.load('images/aliens.bmp')
        self.rect = self.image.get_rect()

        # new alien at top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # store the aliens position
        self.x = float(self.rect.x)

    def blitme(self):
        """Draw the alien at teh current location"""
        self.screen.blit(self.image, self.rect)
