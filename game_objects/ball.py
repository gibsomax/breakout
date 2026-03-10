#this will house the ball.
#it needs to have collisions
#it needs to push another ball into an outer brick upon collision
#also needs to bounce off outer brick upon collision
from settings import ball_size,SCREEN_HEIGHT,SCREEN_WIDTH
import pygame
import random


class BALL:
    def __init__(self):
        self.ball_size = ball_size
        self.ball_surface = pygame.Surface((10,10))
        self.ball_surface.fill((255, 255, 255))
        self.ball_rect = self.ball_surface.get_rect()
        self.ball_rect.center = (500,720)
        self.vx = random.choice([-2,2])
        self.vy = -2
        self.destroy = False

    def update(self):
        self.ball_rect.x += self.vx
        self.ball_rect.y += self.vy
        if self.ball_rect.x < 1:
            self.vx = 2
        if self.ball_rect.right >= SCREEN_WIDTH:
            self.vx = -2
        if self.ball_rect.y < 1:
            self.vy = 2
        if self.ball_rect.bottom >= SCREEN_HEIGHT:
            self.destroy = True


    def draw(self, surface):
        surface.blit(self.ball_surface, self.ball_rect)
