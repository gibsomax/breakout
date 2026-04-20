from breakout_main.settings import ball_size, SCREEN_HEIGHT, SCREEN_WIDTH, ball_speed
import pygame
import random


class BALL:
    """
    Represents the characteristics and current state of the ball object.

    Attributes:
        ball_size (int): How large the ball appears.
        ball_surface (int,int): Bounds of the ball object.
        ball_surface.fill (tuple): Sets the color of the ball object.
        ball_rect (rect): Area used for collisions.
        ball_rect.center (int): Where the center of the fall is located.
        vx (float): The horizontal direction the ball is going to travel.
        vy (int): The vertical direction the ball is going to travel.
        destroy (bool): Whether the ball should be destroyed or not.
        is_inside_time (int): Tracks if the ball was newly added to the inner box.

    Methods:
        update(): Changes the ball object's movement direction or destroy state.
        draw(): Creates the image of the ball object at the corresponding screen position.
    """
    def __init__(self):
        """
        Initializes the ball object.
        """
        self.ball_size = ball_size
        self.ball_surface = pygame.Surface((ball_size, ball_size))
        self.ball_surface.fill((255, 255, 255))
        self.ball_rect = self.ball_surface.get_rect()
        self.ball_rect.center = (SCREEN_WIDTH * .5, SCREEN_HEIGHT * .885)
        self.vx = random.choice([-ball_speed, ball_speed])
        self.vy = -ball_speed
        self.destroy = False
        self.is_inside_time = 20

    def update(self):
        """
        Changes the ball object's movement direction or destroy state.
        """
        self.ball_rect.x += self.vx
        self.ball_rect.y += self.vy
        if self.ball_rect.x < 1:
            self.vx = abs(self.vx)
        if self.ball_rect.right >= SCREEN_WIDTH:
            self.vx = -abs(self.vx)
        if self.ball_rect.y < 1:
            self.vy = abs(self.vy)
        if self.ball_rect.bottom >= SCREEN_HEIGHT:
            self.destroy = True

    def draw(self, surface):
        """
        Creates the image of the ball object at the corresponding position.

        Args:
            surface (surface): Passes the screen the ball will exist on.
        """
        surface.blit(self.ball_surface, self.ball_rect)
