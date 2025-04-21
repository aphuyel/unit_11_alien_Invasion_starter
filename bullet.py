import pygame
from pygame.sprite import Sprite
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class Bullet(pygame.sprite.Sprite):  # Inherit from pygame.sprite.Sprite
    def __init__(self, game: 'AlienInvasion') -> None:
        super().__init__()  # Initialize the Sprite class
        self.game = game
        self.settings = game.settings
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()

        # Load the bullet image and initialize its rectangle
        self.image = pygame.image.load(self.settings.bullet_file)
        self.image = pygame.transform.scale(self.image, 
             (self.settings.bullet_w, self.settings.bullet_h)
             )
        self.rect = self.image.get_rect()

        # Position the bullet at the ship's current position
        self.rect.centerx = game.ship.rect.centerx
        self.rect.top = game.ship.rect.top

        # Store the bullet's position as a float for smooth movement
        self.y = float(self.rect.y)

    def update(self) -> None:
        """Move the bullet up the screen."""
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw(self) -> None:
        """Draw the bullet to the screen."""
        self.screen.blit(self.image, self.rect)