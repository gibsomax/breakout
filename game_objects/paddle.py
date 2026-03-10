#this will house the paddle.
#it needs to be able to be moved left and right with the mouse and/or arrow keys.
#it needs to have collision on the top and sides but allow a ball to pass through on the bottom.
import pygame


def paddle(x, y, box_width, box_height):
    paddle_size_x = box_width * 0.16
    paddle_size_y = box_height * 0.064
    pygame.draw.rect(
        screen,
        (200, 200, 255),
        (x , y , paddle_size_x, paddle_size_y),
        border_radius=int(paddle_size_x * .05))