import pygame.font


class Overlay:
    """A class to build overlay for the screen."""

    def __init__(self, pp_game):
        """Initialize overlay attributes."""
        super().__init__()
        self.screen = pp_game.screen
        self.screen_rect = self.screen.get_rect()
        self.score = pp_game.score


    def draw_score(self):

        transparent_surface = pygame.Surface((self.screen.get_rect().width, self.screen.get_rect().height),
                                             pygame.SRCALPHA)
        rect = transparent_surface.get_rect()
        transparent_surface.fill((0, 0, 0, 255))

        # self.screen.fill('black', rect)

        font = pygame.font.Font(None, 36)
        text = font.render(f"{self.score[0]} : {self.score[1]}", True, (255, 255, 255))
        transparent_surface.blit(text, (560, 20))

        self.screen.blit(transparent_surface, transparent_surface.get_rect())
