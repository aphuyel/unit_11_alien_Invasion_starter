import pygame
from pygame.sprite import Sprite
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class Bullet(Sprite):
    def __init__(self, game: 'AlienInvasion') -> None:
        """
        Initialize the bullet and set its starting position.
        The bullet is created at the ship's position.
        """
        super().__init__()

        self.screen = game.screen
        self.settings = game.settings

        try:
            # Load and scale the bullet image
            self.image = pygame.image.load(self.settings.bullet_file)
            self.image = pygame.transform.scale(self.image, 
                (self.settings.bullet_w, self.settings.bullet_h)
            )
        except FileNotFoundError:
            print(f"Error: Bullet image not found at {self.settings.bullet_file}")
            
            self.image = pygame.Surface((self.settings.bullet_w, self.settings.bullet_h))
            self.image.fill((255, 0, 0))  
        self.rect = self.image.get_rect()

        
        self.rect.centerx = game.ship.rect.centerx  
        self.rect.top = game.ship.rect.top  

        # For more precise control over the bullet's position (float for better movement control)
        self.y = float(self.rect.y)

    def update(self):
        """
        Move the bullet up the screen.
        This method updates the bullet's vertical position.
        """
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

        # Remove bullet when it moves off-screen
        if self.rect.bottom <= 0:
            self.kill()  # Automatically remove from sprite group

    def draw_bullet(self) -> None:
        """
        Draw the bullet at its current position.
        """
        self.screen.blit(self.image, self.rect)