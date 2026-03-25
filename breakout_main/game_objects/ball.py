#it needs to push another ball into an outer brick upon collision
#also needs to bounce off outer brick upon collision
from settings import ball_size,SCREEN_HEIGHT,SCREEN_WIDTH,ball_speed
import pygame
import random

class BALL:
    """
    Represents the characteristics and current state of the ball object.

    Attributes:
        ball_size (int): How large the ball appears.
        ball_surface (?): ?
        ball_surface.fill (?): ?
        ball_rect (?): ?
        ball_rect.center (int): Where the center of the fall is located.
        vx (float): The horizontal direction the ball is going to travel.
        vy (int): The vertical direction the ball is going to travel.
        destroy (bool): Whether the ball should be destroyed or not.

    Methods:
        update(): Changes the ball object's movement direction or destroy state.
        draw(): Creates the image of the ball object at the corresponding screen position.
    """
    def __init__(self):
        """
        Initializes the ball object.
        """
        self.ball_size = ball_size
        self.ball_surface = pygame.Surface((10,10))
        self.ball_surface.fill((255, 255, 255))
        self.ball_rect = self.ball_surface.get_rect()
        self.ball_rect.center = (SCREEN_WIDTH * .5,SCREEN_HEIGHT *.885)
        self.vx = random.choice([-ball_speed,ball_speed])
        self.vy = -ball_speed
        self.destroy = False

    def update(self):
        """
        Changes the ball object's movement direction or destroy state.
        """
        self.ball_rect.x += self.vx
        self.ball_rect.y += self.vy
        if self.ball_rect.x < 1:
            self.vx = ball_speed
        if self.ball_rect.right >= SCREEN_WIDTH:
            self.vx = -ball_speed
        if self.ball_rect.y < 1:
            self.vy = ball_speed
        if self.ball_rect.bottom >= SCREEN_HEIGHT:
            self.destroy = True


    def draw(self, surface):
        """
        Creates the image of the ball object at the corresponding position.

        Args:
            surface (?): ?
        """
        surface.blit(self.ball_surface, self.ball_rect)
