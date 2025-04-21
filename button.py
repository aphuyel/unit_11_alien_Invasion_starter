import pygame.font
from pygame import Rect

class Button:
    """A class to create and manage the play button on the screen.

    This class creates a button that can display a message and be clicked to start the game.
    The button is positioned in the center of the screen.
    """

    def __init__(self, game, msg) -> None:
        """Initialize the button's properties."""
        self.game = game
        self.screen = game.screen
        self.boundaries = game.screen.get_rect()
        self.settings = game.settings
        self.font = pygame.font.Font(self.settings.font_file, self.settings.button_font_size)
        self.rect = Rect(0, 0, self.settings.button_w, self.settings.button_h)
        self.rect.center = self.boundaries.center
        self._prep_msg(msg)

    def _prep_msg(self, msg) -> None:
        """Prepare the message to be displayed on the button."""
        self.msg_image = self.font.render(msg, True, self.settings.text_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw(self) -> None:
        """Draw the button on the screen."""
        self.screen.fill(self.settings.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

    def check_clicked(self, mouse_pos) -> bool:
        """Check if the button has been clicked."""
        if self.rect.collidepoint(mouse_pos):
            return True
        return False