#it needs to have collision on the top and sides but allow a ball to pass through on the bottom.
import pygame
from settings import paddle_rad,SCREEN_WIDTH,SCREEN_HEIGHT

class PADDLE:
    """
    Represents the characteristics and current state of the paddle object.

     Attributes:
        paddle_size_x (int): How wide the paddle is.
        paddle_size_y (int): How tall the paddle is below its starting vertical position.
        paddle_rect (): How wide and tall the paddle is and its starting position.
        rad (int):

     Methods:
         draw(): Creates the image of the paddle object at the corresponding position.
     """
    def __init__(self):
        """
        Initializes the paddle object.
        """
        self.paddle_size_x = SCREEN_WIDTH * 0.16
        self.paddle_size_y = SCREEN_HEIGHT * 0.064

        self.paddle_rect = pygame.Rect(
            SCREEN_WIDTH * 0.419,
            SCREEN_HEIGHT * 0.9,
            self.paddle_size_x,
            self.paddle_size_y
        )

        self.rad = paddle_rad

    def draw(self, surface):
        """
        Creates the image of the paddle object at the corresponding position.

        Args:
            surface ():
        """
        pygame.draw.rect(
            surface,
            (200, 200, 255),
            self.paddle_rect,
            border_radius=self.rad
        )