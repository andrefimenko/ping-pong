import pygame.font

class Overlay:
    """A class to build overlay for the screen."""

    def __init__(self, pp_game, score, ball_speed):
        """Initialize overlay attributes."""
        self.screen = pp_game.screen
        self.screen_rect = self.screen.get_rect()

        self.overlay_surface = pygame.Surface((200, 100))
        self.overlay_surface.fill('white')
        self.overlay_surface.set_alpha(128)

        self.font = pygame.font.SysFont(None, 36)
        text = self.font.render('ass', True, (0, 0, 255))
        self.overlay_surface.blit(text, (10, 10))
