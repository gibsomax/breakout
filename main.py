#this is where the game loop will live
import pygame
import sys
from settings import SCREEN_WIDTH, SCREEN_HEIGHT,ball_size
from game_objects.ball import BALL

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Space Invaders")

#define the clock
clock = pygame.time.Clock()

ball = BALL()

running = True
while running:
    # quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    # restart
    if keys[pygame.K_r]:
        ball = BALL()
    if keys[pygame.K_SPACE]:
        ball.start = True



    # clear screen
    screen.fill((0, 0, 0))

    if ball.start:
        ball.update()
    ball.draw(screen)

    # screen flip
    pygame.display.flip()

    # FPS
    clock.tick(60)

# ---after loop quit---
pygame.quit()
sys.exit()