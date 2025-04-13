import pygame
from typing import TYPE_CHECKING
from bullet import Bullet

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class Arsenal:
    def __init__(self, game: 'AlienInvasion') -> None:
        """
        Initialize the arsenal to store and manage bullets.
        """
        self.game = game
        self.settings = game.settings
        self.arsenal = pygame.sprite.Group()

    def update_arsenal(self) -> None:
        """
        Update the position of all bullets in the arsenal.
        This also removes bullets that go off-screen.
        """
        self.arsenal.update()
        self._remove_bullets_offscreen()

    def _remove_bullets_offscreen(self) -> None:
        """
        Remove bullets from the arsenal if they go off-screen.
        """
        for bullet in self.arsenal.copy():
            if bullet.rect.bottom <= 0:
                self.arsenal.remove(bullet)

    def draw(self) -> None:
        """
        Draw all bullets in the arsenal to the screen.
        """
        for bullet in self.arsenal:
            bullet.draw_bullet()

    def fire_bullet(self) -> bool:
        """
        Fire a bullet if the limit has not been reached.
        This method creates a new bullet and plays the laser sound.
        """
        if len(self.arsenal) < self.settings.bullet_amount:
            new_bullet = Bullet(self.game)
            self.arsenal.add(new_bullet)

            # Play laser sound effect
            laser_sound = pygame.mixer.Sound(str(self.settings.laser_sound))
            laser_sound.set_volume(0.5)
            laser_sound.play()

            return True
        return False