import pygame

class Racket:
    """A class to manage a racket."""

    def __init__(self, pp_game, owner):
        """Initialize a racket and set its starting position."""
        super().__init__()
        self.screen = pp_game.screen
        self.screen_rect = pp_game.screen.get_rect()
        self.settings = pp_game.settings
        self.color = self.settings.racket_color

        # Create a racket rect at (0, 0) and then set correct position.
        self.rect = pygame.Rect(0, 0, self.settings.racket_width,
                                self.settings.racket_height)
        if owner == 1:
            self.rect.midleft = pp_game.screen.get_rect().midleft
        if owner == 2:
            self.rect.midright = pp_game.screen.get_rect().midright

        # Movement flags; start with a racket that's not moving.
        self.moving_up = False
        self.moving_down = False

        # Store the racket's position as a float.
        self.y = float(self.rect.y)

    def update(self):
        """Update the racket's position based on the movement flags."""
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.rect.y -= self.settings.racket_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.y += self.settings.racket_speed

    def center_racket(self):
        """Center rackets on the screen."""
        self.rect.center = self.screen_rect.y / 2

    def draw_racket(self):
        """Draw the racket at its current location."""

        pygame.draw.rect(self.screen, self.color, self.rect)
