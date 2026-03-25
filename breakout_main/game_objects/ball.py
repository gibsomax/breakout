#this will house the ball.
#it needs to have collisions
#it needs to push another ball into an outer brick upon collision
#also needs to bounce off outer brick upon collision
from settings import ball_size,SCREEN_HEIGHT,SCREEN_WIDTH,ball_speed
import pygame
import random

class BALL:
    """
    Description

    Attributes:
        ball_size (int):
        ball_surface ():
        ball_surface.fill ():
        ball_rect ():
        ball_rect.center (int):
        vx ():
        vy ():
        destroy (bool):

    Methods:
        update():
        draw(): Returns the card's suit.
    """
    def __init__(self):
        """
        Description
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
        Description
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
        Description

        Args:
            surface ():
        """
        surface.blit(self.ball_surface, self.ball_rect)
