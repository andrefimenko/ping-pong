import sys

import pygame

from settings import Settings
from racket import Racket
from ball import Ball

class PingPong:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()

        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Ping-Pong")

        self.racket = Racket(self)
        self.ball = Ball(self)

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self.racket.update()
            self.ball.update()
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_UP:
            self.racket.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.racket.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_UP:
            self.racket.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.racket.moving_down = False

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.racket.draw_racket()
        self.ball.draw_ball()

        pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    pp = PingPong()
    pp.run_game()
