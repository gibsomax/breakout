#this is where the game loop will live
import pygame
import sys
from settings import SCREEN_WIDTH, SCREEN_HEIGHT,velocity,paddle_rad,ball_speed
from game_objects.ball import BALL
from game_objects.paddle import PADDLE

#create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Breakout")

#define the clock
clock = pygame.time.Clock()

#init
ball = [BALL()]
ball_destroy = []
start = False
paddle = PADDLE()

#game loop
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
    #starts the ball moving
    if keys[pygame.K_SPACE]:
        start = True

    # exit
    if keys[pygame.K_q]:
        pygame.quit()

    # paddle movement, and ball if it has not started moving yet
    if keys[pygame.K_LEFT] and paddle.paddle_rect.left >= 0+paddle_rad:
        paddle.paddle_rect.x -= velocity
        if not start:
            ball[0].ball_rect.x -= velocity
    if keys[pygame.K_RIGHT] and paddle.paddle_rect.right <= SCREEN_WIDTH-paddle_rad:
        paddle.paddle_rect.x += velocity
        if not start:
            ball[0].ball_rect.x += velocity

    #ball/paddle collision
    for i in ball:
        if paddle.paddle_rect.colliderect(i.ball_rect):
            if i.ball_rect.bottom <= paddle.paddle_rect.top + abs(i.vy):
                i.vy = -ball_speed
            elif i.ball_rect.right <= paddle.paddle_rect.left + abs(i.vy):
                i.vx = -ball_speed
            elif i.ball_rect.left <= paddle.paddle_rect.right + abs(i.vy):
                i.vx = ball_speed



    # clear screen
    screen.fill((0, 0, 0))

    #draw paddle
    paddle.draw(screen)

    #destroys balls when they hit the bottom of the screen
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