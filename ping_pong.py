import sys
import time

import pygame

from settings import Settings
from racket import Racket
from ball import Ball
from score import Score
from button import Button

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
        self.score = Score(self)

        # Start Ping-Pong in an inactive state.
        self.game_active = False

        # Make the Play button.
        self.play_button = Button(self, "Play Ping-Pong")

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()

            if self.game_active:
                self._update_rackets()
                self._update_ball()

            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_play_button(self, mouse_pos):
        """Start a new game when the player clicks Play Ping-Pong."""
        if self.play_button.rect.collidepoint(mouse_pos):
            self.game_active = True

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
        """Spin and speed up the ball if a racket moves and check goals"""

        # Left racket spins
        if self.ball.rect.colliderect(self.p1_racket.rect):
            if self.p1_racket.moving_up:
                self.ball.vert_speed -= self.settings.racket_spin
                self.ball.hor_speed += self.settings.racket_speed_up
            if self.p2_racket.moving_down:
                self.ball.vert_speed += self.settings.racket_spin
                self.ball.hor_speed += self.settings.racket_speed_up
            self.ball.hor_speed *= -1

        # Right racket spins
        if self.ball.rect.colliderect(self.p2_racket.rect):
            if self.p2_racket.moving_up:
                self.ball.vert_speed -= self.settings.racket_spin
                self.ball.hor_speed += self.settings.racket_speed_up
            if self.p2_racket.moving_down:
                self.ball.vert_speed += self.settings.racket_spin
                self.ball.hor_speed += self.settings.racket_speed_up
            self.ball.hor_speed *= -1

        # Check a goal to the left player
        if self.ball.rect.left <= 0:
            self._goal(1)

        # Check a goal to the right player
        if self.ball.rect.right >= self.screen.get_rect().right:
            self._goal(2)

        self.ball.update()

    def _goal(self, player):
        """Scores the game and restarts round with opposite ball direction."""
        if player == 1:
            self.score.score[0] += 1
            print(self.score.score)
        if player == 2:
            self.score.score[1] += 1
            print(self.score.score)

        self.ball.hor_speed *= -1
        self._center_ball()

    def _center_ball(self):
        """Centers the ball and resets its vertical speed."""
        self.ball.rect.center = self.screen.get_rect().center
        self.ball.vert_speed = 0

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.p1_racket.draw_racket()
        self.p2_racket.draw_racket()
        self.ball.draw_ball()

        # Draw the play button if the game is inactive.
        if not self.game_active:
            self.play_button.draw_button()

        pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    pp = PingPong()
    pp.run_game()
