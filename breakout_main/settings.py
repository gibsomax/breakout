"""
Description

Attributes:
    SCREEN_WIDTH (int):
    SCREEN_HEIGHT (int):
    ball_size (int):
    velocity (int):
    paddle_rad (int):
    ball_speed (int)
    default_lives (int)
"""
import pygame
pygame.init()

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
ball_size = 50
velocity = 10
paddle_rad = int(SCREEN_WIDTH * 0.16 * .05)
ball_speed = 4
default_lives = 3