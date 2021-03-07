import pygame


class Ship:
    """A class to mange the ship."""

    def __init__(self, ai_game):
        """Initializing the ship and set its starting position."""
        # pygame treats every element of the game as rectangle
        self.screen = ai_game.screen  # Assigning the screen to the attribute if ship
        self.screen_rect = ai_game.screen.get_rect()
        # we access the screen't re t attribut with get_rectmethod

        # Load the ship image and get its rect.
        self.image = pygame.image.load("ship.bmp")
        self.rect = (
            self.image.get_rect()
        )  ## accessing ships surface rectangle attribute

        # start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Draw the ship to the screen at the position specified by self.rect."""
        self.screen.blit(self.image, self.rect)
