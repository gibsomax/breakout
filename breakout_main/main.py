"""
Contains the game loop. When it is run the player is able to play the game. All variables initialized are used solely within this module. No part of this module is called
    in any other module. This module takes the player inputs, provides score and time feedback, initializes the brick, ball, and paddle, and detects collisions.
"""
import pygame
import sys
from settings import SCREEN_WIDTH, SCREEN_HEIGHT,velocity,paddle_rad,ball_speed, default_lives
from breakout_main.game_objects.ball import BALL
from breakout_main.game_objects.paddle import PADDLE
from breakout_main.game_objects.brick import BRICK

#create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Breakout")
pygame.font.init()
font = pygame.font.SysFont("Arial", 24)

#define the clock
clock = pygame.time.Clock()

#init
ball = [BALL()]
ball_destroy = []
start = False
paddle = PADDLE()

#adding bricks
def create_bricks(rows=8, cols=13, offset_x=18, offset_y=50, padding=4):
    """
    Creates the rows and columns of bricks that can be interacted with using the BRICK object.

    Args:
        rows (int): Determines the number of rows of bricks that will appear on screen.
        cols (int): Determines the number of columns of bricks that will appear on screen.
        offset_x (int): Determines how far from either side of the screen the bricks appear.
        offset_y (int): Determines how far from the top of the screen the bricks appear.
        padding (int): Determines how far from other bricks the bricks appear.

    Returns:
        list: The BRICK objects in a list.
    """
    bricks = []
    brick_w, brick_h = 70, 25
    colors = [(220,50,50),(220, 130, 50),(220,220,50),(50,200,50),(50,100,220)]
    for row in range(rows):
        for col in range(cols):
            x = offset_x + col * (brick_w + padding)
            y = offset_y + row * (brick_h + padding)
            bricks.append(BRICK(x, y, brick_w, brick_h, colors[row % len(colors)]))
    return bricks

bricks = create_bricks()
score = 0
start_time = None

lives = default_lives

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
        bricks = create_bricks()
        paddle = PADDLE()
        score = 0
        start_time = None
        start = False
        lives = default_lives
    #starts the ball moving
    if keys[pygame.K_SPACE] and lives > 0:
        start = True
        if start_time is None:
            start_time = pygame.time.get_ticks()


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
                i.vx = (i.ball_rect.x / 10 - paddle.paddle_rect.center[0] / 10)
            elif i.ball_rect.right <= paddle.paddle_rect.left + abs(i.vy):
                i.vx = -ball_speed
            elif i.ball_rect.left <= paddle.paddle_rect.right + abs(i.vy):
                i.vx = ball_speed

    #ball/brick collision
    for ball_obj in ball:
        for brick in bricks:
            if brick.alive and brick.rect.colliderect(ball_obj.ball_rect):
                brick.hit()
                ball_obj.vy *= -1
                if not brick.alive:
                    score += 100
                break
    bricks = [b for b in bricks if b.alive]

    # clear screen
    screen.fill((0, 0, 0))

    #draw paddle
    paddle.draw(screen)

    # score and timer HUD
    elapsed = (pygame.time.get_ticks() - start_time) // 1000 if start_time else 0
    multiplier = max(1, 10 - elapsed // 60)
    hud = font.render(f"Score: {score} Time: {elapsed} x{multiplier}", True, (255, 255, 255))
    screen.blit(hud, (SCREEN_WIDTH - 400, 10))

    #draw bricks
    for brick in bricks:
        brick.draw(screen)

    #destroys balls when they hit the bottom of the screen
    if start:
        for i in range(len(ball)):
            if ball[i].destroy:
                ball_destroy.append(ball[i])
                lives -= 1
                start = False
                paddle = PADDLE()
            ball[i].update()
    for i in range(len(ball)):
        ball[i].draw(screen)
    for i in ball_destroy:
        ball.remove(i)
        ball = [BALL()]
    ball_destroy.clear()

    #Loss condition
    if lives == 0:
        text = font.render('You Lose! Press R to Restart!', True, (0, 255, 0), (0, 0, 0))
        textRect = text.get_rect()
        textRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        screen.blit(text, textRect)


    #Win condition
    if not bricks:
        start = False
        lives = 0
        text = font.render(f'You won with {score} points! Press R to play again!', True, (0, 255, 0), (0, 0, 0))
        textRect = text.get_rect()
        textRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        screen.blit(text, textRect)

    # screen flip
    pygame.display.flip()

    # FPS
    clock.tick(60)
# ---after loop quit---
pygame.quit()
sys.exit()