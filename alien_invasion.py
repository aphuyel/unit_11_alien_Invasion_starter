"""
Achut Phuyel
Lab 12
04/06/2025
This lab is about the alien invasion game."""
import sys
import pygame
from settings import settings
from ship import Ship

class AlienInvasion:
    def __init__(self) -> None:
        pygame.init()
        self.settings = settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_w, self.settings.screen_h)
        )
        pygame.display.set_caption(self.settings.name)

        self.bg = pygame.image.load(self.settings.bg_file)
        self.bg = pygame.transform.scale(self.bg, 
            (self.settings.screen_w, self.settings.screen_h)
        )
        self.running = True
        self.clock = pygame.time.Clock()

        self.ship = Ship(self)

    def run_game(self) -> None:
        # Game loop
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    sys.exit()

                # Handle key events for the ship
                self.ship.handle_event(event)

            # Update the ship's position based on key press
            self.ship.update()

            # Update game screen
            self.screen.blit(self.bg, (0, 0))  # Draw background
            self.ship.draw()  # Draw the ship
            pygame.display.flip()  # Update the display

            self.clock.tick(self.settings.FPS)  # Control the frame rate

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()

