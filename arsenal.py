import pygame
from typing import TYPE_CHECKING
from bullet import Bullet

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class Arsenal:
    def __init__(self, game: 'AlienInvasion') -> None:
        self.game = game
        self.bullets = pygame.sprite.Group()  # Create a sprite group for bullets

    def fire_bullet(self) -> bool:
        """Create a new bullet and add it to the bullets group."""
        if len(self.bullets) < self.game.settings.bullet_amount:
            new_bullet = Bullet(self.game)  # Create a new bullet
            self.bullets.add(new_bullet)  # Add the bullet to the group
            return True
        return False

    def update_arsenal(self) -> None:
        """Update the positions of the bullets."""
        self.bullets.update()

    def draw(self) -> None:
        """Draw all the bullets to the screen."""
        for bullet in self.bullets.sprites():
            bullet.draw()