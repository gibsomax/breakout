#this is where the game loop will live
import pygame
import sys
from settings import SCREEN_WIDTH, SCREEN_HEIGHT,ball_size
from game_objects.ball import BALL
from Design_template import paddle
from settings import velocity

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Breakout")

#define the clock
clock = pygame.time.Clock()

ball = BALL()
paddle_pos = (SCREEN_WIDTH * .45)
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
    # exit
    if keys[pygame.K_q]:
        pygame.quit()
    # paddle movement
    if keys[pygame.K_LEFT] and paddle_pos > 0:
        paddle_pos = paddle_pos - velocity
        paddle(paddle_pos, SCREEN_HEIGHT * .9, SCREEN_WIDTH, SCREEN_HEIGHT)
        pygame.display.update()
    if keys[pygame.K_RIGHT] and paddle_pos < SCREEN_WIDTH - (SCREEN_WIDTH * 0.16):
        paddle_pos = paddle_pos + velocity
        paddle(paddle_pos, SCREEN_HEIGHT * .9, SCREEN_WIDTH, SCREEN_HEIGHT)
        pygame.display.update()
    else:
        paddle(paddle_pos, SCREEN_HEIGHT * .9, SCREEN_WIDTH, SCREEN_HEIGHT)
        pygame.display.update()


    # clear screen
    screen.fill((0, 0, 0))

    if ball.start:
        ball.update()
    ball.draw(screen)

    # screen flip
    #pygame.display.flip()

    # FPS
    clock.tick(60)

# ---after loop quit---
pygame.quit()
sys.exit()