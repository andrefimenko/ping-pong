import pygame

class Ball:
    """A class to manage the ball."""

    def __init__(self, pp_game):
        """Create a ball object at starting position."""
        super().__init__()
        self.screen = pp_game.screen
        self.screen_rect = pp_game.screen.get_rect()
        self.settings = pp_game.settings
        self.color = self.settings.ball_color

        # Create a ball rect at (0, 0) and then set starting position.
        self.rect = pygame.Rect(0, 0, self.settings.ball_size,
                                self.settings.ball_size)
        self.rect.center = pp_game.screen.get_rect().center

        # Movement flags; start with a ball that's not moving.
        self.hor_speed = 0.0
        self.vert_speed = 0.0

        # Store the ball's coordinates as a floats.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self):
        """Update the ball's position based on the movement flags."""
        self.rect.x += self.hor_speed
        self.rect.y += self.vert_speed

    def draw_ball(self):
        """Draw the boll at its current position."""
        pygame.draw.rect(self.screen, self.color, self.rect)
