import pygame
from settings import Settings
from game_stats import GameStats
from ship import Ship
from arsenal import Arsenal
from alien_fleet import AlienFleet
from time import sleep

class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.stats = GameStats(self.settings.starting_ship_count)
        self.screen = pygame.display.set_mode(
            (self.settings.screen_w, self.settings.screen_h))
        pygame.display.set_caption(self.settings.name)

        self.bg_image = pygame.image.load(self.settings.bg_file)
        self.bg_image = pygame.transform.scale(self.bg_image,
                                                (self.settings.screen_w, self.settings.screen_h))

        self.arsenal = Arsenal(self)
        self.ship = Ship(self, self.arsenal)
        self.alien_fleet = AlienFleet(self)

        self.clock = pygame.time.Clock()

    def run_game(self):
        """Start the main game loop."""
        while True:
            self._check_events()

            self.ship.update()
            self.alien_fleet.update()

            # Check for collisions
            self.check_collisions()

            self._update_screen()
            self.clock.tick(self.settings.FPS)

    def _check_events(self):
        """Handle user input."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            self.ship.handle_event(event)

    def check_collisions(self):
        """Check for bullet-alien and ship-alien collisions."""
        # Check for collisions between bullets and aliens
        collisions = pygame.sprite.groupcollide(self.arsenal.arsenal, self.alien_fleet.fleet, True, True)

        if collisions:
            print(f"Collisions: {collisions}")  # Debugging: prints the collisions

        # Check if the ship collides with any alien
        if pygame.sprite.spritecollideany(self.ship, self.alien_fleet.fleet):
            print("Ship hit!")
            self._handle_ship_hit()

    def _handle_ship_hit(self):
        """Respond to the ship being hit by an alien."""
        print("Handling ship hit...")
        self.stats.ships_left -= 1

        if self.stats.ships_left <= 0:
            self.game_active = False
        else:
            self.ship.rect.centerx = self.screen.get_rect().centerx
            self.ship.rect.bottom = self.screen.get_rect().bottom

            self.arsenal.arsenal.empty()
            self.alien_fleet.reset_fleet()

            sleep(0.5)

    def _update_screen(self):
        """Update the screen and draw all game elements."""
        self.screen.blit(self.bg_image, (0, 0))
        self.ship.draw()
        self.arsenal.draw()
        self.alien_fleet.draw()
        pygame.display.flip()

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()