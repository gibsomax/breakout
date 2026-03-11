#this will house the paddle.
#it needs to be able to be moved left and right with the mouse and/or arrow keys.
#it needs to have collision on the top and sides but allow a ball to pass through on the bottom.
import pygame
from settings import paddle_rad

class PADDLE:
    def __init__(self, box_width, box_height):
        self.paddle_size_x = box_width * 0.16
        self.paddle_size_y = box_height * 0.064

        self.paddle_rect = pygame.Rect(
            box_width * 0.45,
            box_height * 0.9,
            self.paddle_size_x,
            self.paddle_size_y
        )

        self.rad = paddle_rad

    def draw(self, surface):
        pygame.draw.rect(
            surface,
            (200, 200, 255),
            self.paddle_rect,
            border_radius=self.rad
        )


