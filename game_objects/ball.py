#this will house the ball.
#it needs to have collisions
#it needs to push another ball into an outer brick upon collision
#also needs to bounce off outer brick upon collision
from settings import ball_size
import pygame


class BALL:
    def __init__(self):
        self.ball_size = ball_size
        self.ball_surface = pygame.Surface((10,10))
        self.ball_surface.fill((255, 255, 255))
        self.ball_rect = self.ball_surface.get_rect()

    def draw(self, surface):
        surface.blit(self.ball_surface, self.ball_rect)
