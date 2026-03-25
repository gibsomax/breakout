#this will be a place to adjust things like ball speed, window size etc.
import pygame
pygame.init()

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
ball_size = 50
velocity = 10
paddle_rad = int(SCREEN_WIDTH * 0.16 * .05)
ball_speed = 4
default_lives = 3