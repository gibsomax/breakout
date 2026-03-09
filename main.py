#this is where the game loop will live
import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Space Invaders")

#define the clock
clock = pygame.time.Clock()


running = True

while running:
    # quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
