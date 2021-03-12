class Settings:
    """A class to store all settings for Alien Invasion"""

    def __init__(self):
        """Initializaing game settings"""
        self.screen_width = 1200  # not needed after keeping in full screen
        self.screen_height = 600  # not needed after keeping in full screen
        self.bg_color = (230, 230, 230)  ## tuple
        self.ship_speed = 1.5

        # Bullet Settings
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 3

        # Alien Settings
        self.alien_speed = 1.0
