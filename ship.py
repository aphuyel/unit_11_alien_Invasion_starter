import pygame
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion
    from arsenal import Arsenal

class Ship:
    def __init__(self, game: 'AlienInvasion', arsenal: 'Arsenal') -> None:
        self.game = game
        self.settings = game.settings
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()

        self.image = pygame.image.load(self.settings.ship_file)
        self.image = pygame.transform.scale(self.image, 
             (self.settings.ship_w, self.settings.ship_h)
             )
        self.rect = self.image.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Movement flags
        self.moving_up = False
        self.moving_down = False
        self.moving_left = False
        self.moving_right = False
        self.arsenal = arsenal

    def update(self) -> None:
        """Update the ship's position based on movement flags."""
        self._update_ship_movement()
        self.arsenal.update_arsenal()

    def _update_ship_movement(self):
        if self.moving_up and self.rect.top > 0:
            self.rect.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.y += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.rect.x -= self.settings.ship_speed
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.x += self.settings.ship_speed

    def draw(self) -> None:
        """Draw the ship at its current position."""
        self.screen.blit(self.image, self.rect)

    def handle_event(self, event) -> None:
        """Handle key events for moving the ship."""
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.moving_up = True
            if event.key == pygame.K_DOWN:
                self.moving_down = True
            if event.key == pygame.K_LEFT:
                self.moving_left = True
            if event.key == pygame.K_RIGHT:
                self.moving_right = True
            if event.key == pygame.K_SPACE:
                self.fire()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                self.moving_up = False
            if event.key == pygame.K_DOWN:
                self.moving_down = False
            if event.key == pygame.K_LEFT:
                self.moving_left = False
            if event.key == pygame.K_RIGHT:
                self.moving_right = False

    def fire(self) -> None:
        if self.arsenal.fire_bullet():
            print("Firing bullet...")  # Debugging
            sound = pygame.mixer.Sound(str(self.settings.laser_sound))
            sound.set_volume(0.5)
            sound.play()