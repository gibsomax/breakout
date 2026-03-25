#this will house the paddle.
#it needs to be able to be moved left and right with the mouse and/or arrow keys.
#it needs to have collision on the top and sides but allow a ball to pass through on the bottom.
import pygame
from settings import paddle_rad,SCREEN_WIDTH,SCREEN_HEIGHT

class PADDLE:
    """
    Description

     Attributes:

     Methods:
         draw(): Returns the card's suit.
     """
    def __init__(self):
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
        A white rectangle is frawn
        """
        pygame.draw.rect(
            surface,
            (200, 200, 255),
            self.paddle_rect,
            border_radius=self.rad
        )


