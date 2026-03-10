#this is where the game loop will live
import pygame
import sys
from settings import SCREEN_WIDTH, SCREEN_HEIGHT
from game_objects.ball import BALL

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Breakout")

#define the clock
clock = pygame.time.Clock()

ball = [BALL()]
ball_destroy = []
start = False

running = True
while running:
    # quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    # restart
    if keys[pygame.K_r]:
        ball = [BALL()]
        start = False
    if keys[pygame.K_SPACE]:
        start = True



    # clear screen
    screen.fill((0, 0, 0))

    if start:
        for i in range(len(ball)):
            if ball[i].destroy:
                ball_destroy.append(ball[i])
            ball[i].update()
    for i in range(len(ball)):
        ball[i].draw(screen)
    for i in ball_destroy:
        ball.remove(i)
    ball_destroy.clear()

    # screen flip
    pygame.display.flip()

    # FPS
    clock.tick(60)

# ---after loop quit---
pygame.quit()
sys.exit()