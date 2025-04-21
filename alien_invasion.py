import pygame
import sys
from pygame.sprite import Group
from settings import Settings
from ship import Ship
from alien import Alien
from bullet import Bullet
from arsenal import Arsenal
from button import Button
from game_stats import GameStats
from hud import HUD

class AlienInvasion:  
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_w, self.settings.screen_h)
        )
        pygame.display.set_caption(self.settings.name)

        # Initialize game components
        self.game_stats = GameStats(self)
        self.hud = HUD(self)
        
        # Create Arsenal instance
        self.arsenal = Arsenal(self)
        
        # Create Ship instance and pass Arsenal
        self.ship = Ship(self, self.arsenal)
        
        # Create a group for aliens and bullets
        self.aliens = Group()
        self.bullets = Group()
        
        # Create Play button
        self.button = Button(self, "Play")
        
        # Create the alien fleet
        self._create_fleet()
        
        # Initialize the game clock
        self.clock = pygame.time.Clock()

    def _create_fleet(self):
        """Create a fleet of aliens."""
        alien = Alien(self, x=100, y=100)  # Example position for the first alien
        self.aliens.add(alien)
        
        # You can create a grid of aliens if you want:
        # Here’s an example of creating a simple grid of aliens:
        for row in range(3):
            for col in range(5):
                x = 100 + col * 80  # Adjust x to space aliens horizontally
                y = 100 + row * 60  # Adjust y to space aliens vertically
                alien = Alien(self, x=x, y=y)
                self.aliens.add(alien)

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self.ship.update()
            self.arsenal.update_arsenal()  # Update the bullets' positions
            self._update_screen()
            self._update_screen()
            self.clock.tick(self.settings.FPS)

    def _check_events(self):
        """Check for keyboard and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                self.ship.handle_event(event)
            elif event.type == pygame.KEYUP:
                self.ship.handle_event(event)

    def _update_screen(self):
        """Update the screen and draw everything."""
        self.screen.fill(self.settings.bg_color)
        
        # Draw all the sprites (including the ship and aliens)
        self.ship.update()
        self.ship.draw()
        
        # Draw aliens
        for alien in self.aliens:
            alien.draw()
        
        # Draw the HUD (score, level, lives)
        self.hud.draw()
        
        # Draw the play button if the game is inactive
        if not self.game_stats.game_active:
            self.button.draw()
            self.screen.fill(self.settings.bg_color)
        self.ship.draw()
        self.arsenal.draw()
        pygame.display.flip()     
    def _check_collisions(self):
         collisions = pygame.sprite.groupcollide(self.arsenal.bullets, self.aliens, True, True)
         if collisions:
            for aliens in collisions.values():
                self.game_stats.score += 10 
if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()