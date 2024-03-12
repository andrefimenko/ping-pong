class Settings:
    """A class to store all settings for Ping-Pong."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = 'black'

        # Racket settings
        self.racket_speed = 20.0
        self.racket_width = 30
        self.racket_height = 150
        self.racket_color = 'white'

        # Ball settings
        self.ball_hor_speed = 10.0
        self.ball_vert_speed = 5
        self.ball_size = 30
        self.ball_color = 'white'
