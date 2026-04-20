"""
Stores variables called in multiple modules that are largely unchanging.

Attributes:
    SCREEN_WIDTH (int): How wide the window the game is played in appears.
    SCREEN_HEIGHT (int): How long the windows the game is played in appears.
    ball_size (int): How large the ball appears.
    velocity (int): How fast the paddle moves.
    paddle_rad (int): How longs the paddle appears.
    ball_speed (int): How fast the ball moves.
    default_lives (int): How many times the ball can be destroyed before the game ends.
"""
import pygame
pygame.init()

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
ball_size = 5
velocity = 17
paddle_rad = int(SCREEN_WIDTH * 0.16 * .05)
ball_speed = 3
default_lives = 3
