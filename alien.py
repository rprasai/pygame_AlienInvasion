import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """A Class to represent a single alien in the fleet."""

    def __init__(self, ai_game):
        """Initialize teh alien and set its starting position"""
        super().__init__()
        self.screen = ai_game.screen

        # Load the alien image and set its rect attribute
        self.image = pygame.image.load("alien.bmp")
        self.rect = self.image.get_rect()

        # start each new alien near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # store the alien's exact horizonatal position
        self.x = float(self.rect.x)