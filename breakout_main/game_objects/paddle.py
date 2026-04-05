#it needs to have collision on the top and sides but allow a ball to pass through on the bottom.
import pygame
from breakout_main.settings import paddle_rad,SCREEN_WIDTH,SCREEN_HEIGHT

class PADDLE:
    """
    Represents the characteristics and current state of the paddle object.

     Attributes:
        paddle_size_x (int): How wide the paddle is.
        paddle_size_y (int): How tall the paddle is below its starting vertical position.
        paddle_rect (rect): How wide and tall the paddle is and its starting position.
        rad (int): How large the radius of the paddle corners are.

     Methods:
         draw(): Creates the image of the paddle object at the corresponding position.
     """
    def __init__(self,paddle_size_x,paddle_size_y,x,y,rad=paddle_rad):
        """
        Initializes the paddle object.
        """

        self.incr = .0
        self.paddle_rect = pygame.Rect(
            x,
            y,
            paddle_size_x,
            paddle_size_y
        )

        self.rad = rad

    def draw(self, surface):
        """
        Creates the image of the paddle object at the corresponding position.

        Args:
            surface (surface): Passes the screen the paddle will exist on.
        """
        pygame.draw.rect(
            surface,
            (200, 200, 255),
            self.paddle_rect,
            border_radius=self.rad
        )