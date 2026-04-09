"""
Contains the game loop. When it is run the player is able to play the game. All variables initialized are used solely within this module. No part of this module is called
    in any other module. This module takes the player inputs, provides score and time feedback, initializes the brick, ball, and paddle, and detects collisions.
"""
import copy
import pygame
import sys
from breakout_main.settings import SCREEN_WIDTH, SCREEN_HEIGHT,velocity,paddle_rad,ball_speed, default_lives
from breakout_main.game_objects.ball import BALL
from breakout_main.game_objects.paddle import PADDLE
from breakout_main.game_objects.brick import BRICK
from breakout_main.game_objects.inner_box import INNERBOX

def main():
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
    paddle = PADDLE(SCREEN_WIDTH * 0.16,SCREEN_HEIGHT * 0.064,SCREEN_WIDTH * 0.419, SCREEN_HEIGHT * 0.9)
    #set up inner box
    inner_boxes = []
    inner_paddles = []
    offset_x = SCREEN_WIDTH * 0.23 + 15
    offset_y = SCREEN_HEIGHT * 0.18 + 15
    for i in range(4):
        for j in range(2):
            inner_boxes.append(INNERBOX((SCREEN_WIDTH*.018) + (i * offset_x),(SCREEN_HEIGHT*.054) + (j * offset_y)))
    for i in inner_boxes:
        inner_paddles.append((PADDLE(SCREEN_WIDTH * 0.05,SCREEN_HEIGHT * 0.01,i.box_rect_top.left +(i.box_rect_bottom.width * 0.395), i.box_rect_top.top + (i.box_rect_left.height * 0.9),1)))
        i.paddle = inner_paddles[-1]


    #adding bricks
    def create_bricks(rows=3, cols=10, offset_x=8, offset_y=8, padding=2):
        """
        Creates the rows and columns of bricks that can be interacted with using the BRICK object.

        Args:
            rows (int): The number of rows of bricks that will appear on screen.
            cols (int): The number of columns of bricks that will appear on screen.
            offset_x (int): How far from either side of the screen the bricks appear.
            offset_y (int): How far from the top of the screen the bricks appear.
            padding (int): How far from other bricks the bricks appear.

        Returns:
            list: The BRICK objects in a list.
        """
        bricks = []
        brick_w, brick_h = 20, 8
        colors = [(220,50,50),(220, 130, 50),(220,220,50),(50,200,50),(50,100,220)]
        for i in inner_boxes:
            for row in range(rows):
                for col in range(cols):
                    x = offset_x + col * (brick_w + padding) + i.box_rect_top.left
                    y = offset_y + row * (brick_h + padding) + i.box_rect_top.top
                    bricks.append(BRICK(x, y, brick_w, brick_h, colors[row % len(colors)]))
                    i.bricks.append(bricks[-1])
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
            inner_boxes.clear()
            for i in range(4):
                for j in range(2):
                    inner_boxes.append(
                        INNERBOX((SCREEN_WIDTH * .018) + (i * offset_x), (SCREEN_HEIGHT * .054) + (j * offset_y)))
            ball = [BALL()]
            bricks = create_bricks()
            paddle = PADDLE(SCREEN_WIDTH * 0.16,SCREEN_HEIGHT * 0.064,SCREEN_WIDTH * 0.419, SCREEN_HEIGHT * 0.9)
            score = 0
            start_time = None
            start = False
            lives = default_lives
            inner_paddles.clear()
            for i in inner_boxes:
                inner_paddles.append((PADDLE(SCREEN_WIDTH * 0.0299, SCREEN_HEIGHT * 0.01,
                                             i.box_rect_top.left + (i.box_rect_bottom.width * 0.438),
                                             i.box_rect_top.top + (i.box_rect_left.height * 0.9), 1)))
                i.paddle = inner_paddles[-1]
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
            for i in inner_paddles:
                if i.incr < 1:
                    i.paddle_rect.x -= 3
                    i.incr += .6
                else:
                    i.paddle_rect.x -= 4
                    i.incr = 0
            if not start:
                ball[0].ball_rect.x -= velocity
        if keys[pygame.K_RIGHT] and paddle.paddle_rect.right <= SCREEN_WIDTH-paddle_rad:
            paddle.paddle_rect.x += velocity
            for i in inner_paddles:
                if i.incr < 1:
                    i.paddle_rect.x += 3
                    i.incr += .6
                else:
                    i.paddle_rect.x += 4
                    i.incr = 0
            if not start:
                ball[0].ball_rect.x += velocity

        #outside ball/paddle collision
        for i in ball:
            if paddle.paddle_rect.colliderect(i.ball_rect):
                if i.ball_rect.bottom <= paddle.paddle_rect.top + abs(i.vy):
                    i.vy = -ball_speed
                    i.vx = (i.ball_rect.x / 10 - paddle.paddle_rect.center[0] / 10)
                elif i.ball_rect.right <= paddle.paddle_rect.left + abs(i.vy):
                    i.vy = -ball_speed
                    i.vx = (i.ball_rect.x / 10 - paddle.paddle_rect.center[0] / 10)
                elif i.ball_rect.left <= paddle.paddle_rect.right + abs(i.vy):
                    i.vy = -ball_speed
                    i.vx = (i.ball_rect.x / 10 - paddle.paddle_rect.center[0] / 10)

        #inside ball/paddle collision
        for j in inner_boxes:
            for i in j.ball:
                for k in inner_paddles:
                    if k.paddle_rect.colliderect(i.ball_rect):
                        if i.ball_rect.bottom <= paddle.paddle_rect.top + abs(i.vy):
                            i.vy = -i.vy
                            i.vx = (i.ball_rect.x / 10 - k.paddle_rect.center[0] / 10)
                        elif i.ball_rect.right <= k.paddle_rect.left + abs(i.vy):
                            i.vx = -i.vy
                        elif i.ball_rect.left <= k.paddle_rect.right + abs(i.vy):
                            i.vx = i.vy

        #outside ball collisions with inside box
        for i in ball:
            for j in inner_boxes:
                if j.box_rect_bottom.colliderect(i.ball_rect) and i.is_inside == False:
                    ball_copy = copy.copy(i)
                    ball_copy.ball_rect = i.ball_rect.copy()
                    ball_copy.ball_rect.y -= 5
                    ball_copy.vx //= 4
                    ball_copy.vy //= 4
                    ball_copy.is_inside = True
                    j.ball.append(ball_copy)
                    i.vy = abs(i.vy)


        #inside ball collisions with inside box
        for j in inner_boxes:
            for i in j.ball:
                if j.box_rect_bottom.colliderect(i.ball_rect) and i.is_inside == True:
                    j.ball_destroy.append(i)
                if i.ball_rect.x > j.box_rect_right[0] + 4:
                    j.ball_destroy.append(i)
                if i.ball_rect.x < j.box_rect_left[0] - 4:
                    j.ball_destroy.append(i)
                if i.ball_rect.y < j.box_rect_top[1] - 9:
                    j.ball_destroy.append(i)
                if i.ball_rect.y > j.box_rect_bottom[1] + 4:
                    j.ball_destroy.append(i)
                if j.box_rect_top.colliderect(i.ball_rect) and i.is_inside == True:
                    i.vy = abs(i.vy)
                if j.box_rect_right.colliderect(i.ball_rect) and i.is_inside == True:
                    i.vx = -abs(i.vx)
                if j.box_rect_left.colliderect(i.ball_rect) and i.is_inside == True:
                    i.vx = abs(i.vx)
            for i in j.ball_destroy:
                if i in j.ball:
                    j.ball.remove(i)
            j.ball_destroy.clear()

        #ball/brick collision
        for j in inner_boxes:
            for ball_obj in j.ball:
                for brick in bricks:
                    if brick.alive and brick.rect.colliderect(ball_obj.ball_rect):
                        brick.hit()
                        ball_obj.vy *= -1
                        if brick in j.bricks:
                            j.bricks.remove(brick)
                        if not brick.alive:
                            score += 100
                        if not j.bricks:
                            for i in j.ball:
                                ball.append(i)
                            inner_boxes.remove(j)
                        break
            bricks = [b for b in bricks if b.alive]

        #clear screen
        screen.fill((0, 0, 0))

        #draw inner box
        for i in inner_boxes:
            i.draw(screen)

        #draw paddles
        paddle.draw(screen)
        for i in inner_paddles:
            for j in inner_boxes:
                if j.paddle == i:
                    i.draw(screen)

        # score, life, and timer HUD
        elapsed = (pygame.time.get_ticks() - start_time) // 1000 if start_time else 0
        multiplier = max(1, 10 - elapsed // 60)
        hud = font.render(f"Score: {score} Time: {elapsed} x{multiplier}", True, (255, 255, 255))
        lives_indicator = font.render(f"Lives: {lives}", True, (255, 255, 255))
        screen.blit(hud, (SCREEN_WIDTH - 400, 10))
        screen.blit(lives_indicator, (SCREEN_WIDTH - 150, 10))

        #draw bricks
        for brick in bricks:
            for j in inner_boxes:
                if brick in j.bricks:
                    brick.draw(screen)

        #destroys balls when they hit the bottom of the screen
        if start:
            for i in range(len(ball)):
                if ball[i].destroy:
                    ball_destroy.append(ball[i])
                    lives -= 1
                    start = False
                    paddle = PADDLE(SCREEN_WIDTH * 0.16,SCREEN_HEIGHT * 0.064,SCREEN_WIDTH * 0.419, SCREEN_HEIGHT * 0.9)
                    for j in inner_boxes:
                        for k in j.ball:
                            j.ball_destroy.append(k)
                ball[i].update()
        for i in range(len(ball)):
            if lives > 0 and bricks:
                ball[i].draw(screen)
        for i in ball_destroy:
            ball.remove(i)
            ball = [BALL()]
            inner_paddles.clear()
            for i in inner_boxes:
                inner_paddles.append((PADDLE(SCREEN_WIDTH * 0.05, SCREEN_HEIGHT * 0.01,
                                             i.box_rect_top.left + (i.box_rect_bottom.width * 0.395),
                                             i.box_rect_top.top + (i.box_rect_left.height * 0.9), 1)))
                i.paddle = inner_paddles[-1]
        ball_destroy.clear()

        for i in inner_boxes:
            for j in i.ball:
                j.update()
                j.draw(screen)


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


if __name__ == "__main__":
    main()