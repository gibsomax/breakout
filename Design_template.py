import pygame

pygame.init()

SCREEN_WIDTH = 1840
SCREEN_HEIGHT = 1000

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Design Sample")

running = True

#neon test colors (provided by AI)
NEON_COLORS = [
    # Neon Cyan / Teal
    (0, 255, 255),
    (0, 220, 255),
    (0, 255, 200),
    (64, 255, 255),

    # Neon Pink / Magenta
    (255, 0, 255),
    (255, 0, 128),
    (255, 64, 192),
    (255, 51, 153),

    # Neon Purple
    (180, 0, 255),
    (200, 64, 255),
    (138, 43, 226),

    # Neon Blue
    (0, 128, 255),
    (0, 64, 255),
    (64, 128, 255),

    # Neon Green
    (0, 255, 128),
    (57, 255, 20),
    (0, 255, 64),

    # Neon Yellow / Orange
    (255, 255, 0),
    (255, 204, 0),
    (255, 128, 0),

    # UI / Glow-Friendly Whites
    (220, 220, 255),
    (200, 200, 255),
    (180, 255, 255),
]
DARK_NEON_COLORS = [
    # Dark Cyan / Teal
    (0, 90, 90),
    (0, 110, 120),
    (10, 120, 110),
    (30, 140, 140),

    # Dark Pink / Magenta
    (120, 0, 80),
    (140, 0, 100),
    (160, 40, 120),
    (180, 30, 110),

    # Dark Purple
    (90, 0, 130),
    (110, 30, 150),
    (80, 40, 120),

    # Dark Blue
    (0, 60, 120),
    (0, 40, 100),
    (40, 80, 140),

    # Dark Green
    (0, 100, 60),
    (30, 120, 50),
    (0, 120, 40),

    # Dark Yellow / Orange
    (140, 120, 0),
    (160, 110, 20),
    (160, 90, 30),
]
#list of colors for inner boxes
inner_box_color = [(0, 110, 120),(160, 40, 120),(80, 40, 120),(0, 60, 120),(0, 100, 60),(140, 120, 0),(160, 90, 30),(140, 0, 120)]

def brick(x,y,box_width, box_height):
    brick_size_x = box_width * 0.068
    brick_size_y = box_height * 0.064
    spacing_x = brick_size_x * 0.16
    spacing_y = brick_size_y * 0.16

    for j in range(5):
        for i in range(12):
            pygame.draw.rect(
            screen,
            (200, 200, 255),
            (x + (brick_size_x + spacing_x) * i, y + (brick_size_y + spacing_y) * j, brick_size_x, brick_size_y),
            border_radius=int(brick_size_x*.1))

def paddle(x, y, box_width, box_height):
    paddle_size_x = box_width * 0.16
    paddle_size_y = box_height * 0.064
    pygame.draw.rect(
        screen,
        (200, 200, 255),
        (x , y , paddle_size_x, paddle_size_y),
        border_radius=int(paddle_size_x * .05))

def inner_box(box_x,box_y,color=(0,0,0)):
    box_size_x = SCREEN_WIDTH * 0.235    # 23.5% of screen width
    box_size_y = SCREEN_HEIGHT * 0.235   # 23.5% of screen height
    spacing_x = box_size_x * 0.05  # 5% of box width
    spacing_y = box_size_y * 0.05  # 5% of box height
    border_radius_outer = int(box_size_x * 0.02)  # 2% of box width
    border_radius_inner = int(box_size_x * 0.018)  # slightly smaller
    offset_x = box_size_x * 0.007
    offset_y = box_size_y * 0.01

    for j in range(2):
        for i in range(4):
            #draw border
            pygame.draw.rect(
            screen,
            (200, 200, 255) ,
            (box_x + (box_size_x + spacing_x) * i, box_y + (box_size_y + spacing_y) * j, box_size_x, box_size_y),
             border_radius = border_radius_outer)

            #draw box
            pygame.draw.rect(
            screen,
            color[j*4+i],
            (box_x + ((box_size_x + spacing_x) * i) + offset_x, box_y + ((box_size_y + spacing_y) * j) + offset_y, box_size_x - 2 * offset_x, box_size_y - 2 * offset_y),
             border_radius = border_radius_inner)

            #draw brick
            brick(box_x + ((box_size_x + spacing_x) * i) + box_size_x*.03, box_y + ((box_size_y + spacing_y) * j) + box_size_y * 0.042,box_size_x,box_size_y)

            #draw paddle
            paddle((box_x + (box_size_x + spacing_x) * i) +box_size_x*.45 , (box_y + (box_size_y + spacing_y) * j) + box_size_y * .9, box_size_x, box_size_y)



while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 15))
    inner_box(25,25,inner_box_color)
    paddle(SCREEN_WIDTH * .45, SCREEN_HEIGHT * .9, SCREEN_WIDTH, SCREEN_HEIGHT)


    pygame.display.flip()