import pygame

class Racket:
    """A class to manage the racket."""

    def __init__(self, pp_game):
        """Initialize the racket and set its starting position."""
        super().__init__()
        self.screen = pp_game.screen
        self.settings = pp_game.settings
        self.color = self.settings.racket_color

        # Create a racket rect at (0, 0) and then set correct position.
        self.rect = pygame.Rect(0, 0, self.settings.racket_width,
                                self.settings.racket_height)
        self.rect.midleft = pp_game.screen.rect.midleft

        # Store the racket's position as a float.
        self.y = float(self.rect.y)
