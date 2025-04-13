import pygame
from typing import TYPE_CHECKING
from alien import Alien

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class AlienFleet:
    def __init__(self, game: 'AlienInvasion'):
        self.game = game
        self.settings = game.settings
        self.screen_rect = self.game.screen.get_rect()
        self.fleet = pygame.sprite.Group()
        self._create_fleet()

    def _create_fleet(self):
        """Create a fleet of aliens starting from the top row."""
        alien_width = self.settings.alien_w
        alien_height = self.settings.alien_h
        available_space_x = self.screen_rect.width
        available_space_y = self.screen_rect.height // 3  # Adjust height for the fleet

        number_of_aliens_x = available_space_x // alien_width
        number_of_aliens_y = min(5, (self.screen_rect.height // 3) // alien_height)

        for row in range(number_of_aliens_y):
            for alien_num in range(number_of_aliens_x):
                x_position = alien_num * alien_width
                y_position = row * alien_height
                self._create_alien(x_position, y_position)

    def _create_alien(self, x, y):
        """Create an alien at the specified position."""
        alien = Alien(self.game, x, y)
        self.fleet.add(alien)

    def reset_fleet(self):
        """Reset the fleet of aliens to the top row."""
        self.fleet.empty()
        self._create_fleet()

    def update(self):
        """Update the alien fleet's positions."""
        self.fleet.update()

    def draw(self):
        """Draw the aliens to the screen."""
        for alien in self.fleet:
            alien.draw_alien()