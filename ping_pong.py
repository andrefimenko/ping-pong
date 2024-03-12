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

        # Instances of Racket: 1 - left player, 2 - right player
        self.p1_racket = Racket(self, 1)
        self.p2_racket = Racket(self, 2)
        self.ball = Ball(self)

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self._update_rackets()
            self._update_ball()

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
        if event.key == pygame.K_w:
            self.p1_racket.moving_up = True
        elif event.key == pygame.K_UP:
            self.p2_racket.moving_up = True
        elif event.key == pygame.K_s:
            self.p1_racket.moving_down = True
        elif event.key == pygame.K_DOWN:
            self.p2_racket.moving_down = True
        elif event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
            sys.exit()

    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_w:
            self.p1_racket.moving_up = False
        elif event.key == pygame.K_UP:
            self.p2_racket.moving_up = False
        elif event.key == pygame.K_s:
            self.p1_racket.moving_down = False
        elif event.key == pygame.K_DOWN:
            self.p2_racket.moving_down = False

    def _update_rackets(self):

        self.p1_racket.update()
        self.p2_racket.update()

    def _update_ball(self):

        if self.ball.rect.colliderect(self.p1_racket.rect):
            self.ball.hor_speed *= -1
        if self.ball.rect.colliderect(self.p2_racket.rect):
            self.ball.hor_speed *= -1
        self.ball.update()

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.p1_racket.draw_racket()
        self.p2_racket.draw_racket()
        self.ball.draw_ball()

        pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    pp = PingPong()
    pp.run_game()
