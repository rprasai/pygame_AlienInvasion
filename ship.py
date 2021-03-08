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

        self.settings = ai_game.settings

        # start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        # store a decimal value form the ship's horizontal position.
        self.x = float(self.rect.x)

        ##movement
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ship's position based on the movement Flag"""
        # update the ship's x value, not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # update rect object from the self.x
        self.rect.x = self.x

    def blitme(self):
        """Draw the ship to the screen at the position specified by self.rect."""
        self.screen.blit(self.image, self.rect)
