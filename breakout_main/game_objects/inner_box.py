import pygame
from breakout_main.settings import SCREEN_WIDTH, SCREEN_HEIGHT


class INNERBOX:
    """
    Represents the characteristics and current state of the innerbox object.

    Attributes:
        box_size_x (int): How wide the box is.
        box_size_y (int): How tall the box is below its starting vertical position.
        ball (list): List of the balls currently in the box.
        ball_destroy (list): List of balls in the inner box set to be destroyed.
        bricks (list): List of the bricks in the inner box.
        paddle (paddle): Paddle belonging to the inner box.

    Methods:
        draw(): Creates the image of the inner box object at the corresponding position.
    """
    def __init__(self, x, y):

        """
        Initializes the inner box object.
        """
        self.box_size_x = SCREEN_WIDTH * 0.23
        self.box_size_y = SCREEN_HEIGHT * 0.18
        self.ball = []
        self.ball_destroy = []
        self.bricks = []
        self.paddle = None

        self.box_rect_top = pygame.Rect(
            x,
            y,
            self.box_size_x,
            3)
        self.box_rect_bottom = pygame.Rect(
            x,
            y + self.box_size_y,
            self.box_size_x + 3,
            3)
        self.box_rect_left = pygame.Rect(
            x,
            y,
            3,
            self.box_size_y)
        self.box_rect_right = pygame.Rect(
            x + self.box_size_x,
            y,
            3,
            self.box_size_y)

    def draw(self, surface):
        """
        Creates the image of the inner box object at the corresponding position.

        Args:
            surface (surface): Passes the screen the inner box will exist on.
        """
        pygame.draw.rect(
            surface,
            (200, 200, 255),
            self.box_rect_top)
        pygame.draw.rect(
            surface,
            (200, 200, 255),
            self.box_rect_bottom)
        pygame.draw.rect(
            surface,
            (200, 200, 255),
            self.box_rect_left)
        pygame.draw.rect(
            surface,
            (200, 200, 255),
            self.box_rect_right)
