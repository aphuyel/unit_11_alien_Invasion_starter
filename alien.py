import pygame
from pygame.sprite import Sprite
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class Alien(pygame.sprite.Sprite):  # Inherit from pygame.sprite.Sprite
    def __init__(self, game, x, y):
        super().__init__()  # Call the parent class constructor
        self.game = game
        self.settings = game.settings
        self.screen = game.screen
        self.image = pygame.image.load(self.settings.alien_file)
        self.image = pygame.transform.scale(self.image, (self.settings.alien_w, self.settings.alien_h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        """Update the alien's position."""
        self.rect.x += self.settings.fleet_speed * self.settings.fleet_direction

    def draw(self):
        """Draw the alien on the screen."""
        self.screen.blit(self.image, self.rect)