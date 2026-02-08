#this code was writen with the help of AI tools and is intended as a practice and reference for the final project

import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("epilepsy simulator")

box_x,box_y = 350,250
box_size = 100
color = (0,0,0)
running = True

frame_count = 0
vx = 2
vy = 2

clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    frame_count += 1
    if frame_count >= 3:
        if color == (0,0,0):
            color = (255,255,255)
        else:
            color = (0,0,0)
        frame_count = 0

    box_x += vx
    box_y += vy

    if box_x < 1:
        vx = 2
    if box_x + box_size >= SCREEN_WIDTH:
        vx = -2
    if box_y < 1:
        vy = 2
    if box_y + box_size >= SCREEN_HEIGHT:
        vy = -2

    screen.fill((255,0,0))
    pygame.draw.rect(screen,color,(box_x,box_y,box_size,box_size))
    pygame.display.flip()

    clock.tick(60)
pygame.quit()
