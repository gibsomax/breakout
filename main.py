#this is where the game loop will live
import pygame
import sys
from settings import SCREEN_WIDTH, SCREEN_HEIGHT,velocity,paddle_rad
from game_objects.ball import BALL
from game_objects.paddle import PADDLE


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Breakout")

#define the clock
clock = pygame.time.Clock()

ball = [BALL()]
ball_destroy = []
start = False
paddle = PADDLE(SCREEN_WIDTH,SCREEN_HEIGHT)


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

    # exit
    if keys[pygame.K_q]:
        pygame.quit()

    # paddle movement
    if keys[pygame.K_LEFT] and paddle.paddle_rect.left >= 0+paddle_rad:
        paddle.paddle_rect.x -= velocity
    if keys[pygame.K_RIGHT] and paddle.paddle_rect.right <= SCREEN_WIDTH-paddle_rad:
        paddle.paddle_rect.x += velocity



    # clear screen
    screen.fill((0, 0, 0))

    #draw paddle
    paddle.draw(screen)

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