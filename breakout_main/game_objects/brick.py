import pygame

class BRICK:
    """
    Represents the characteristics and current state of the brick objects.

    Attributes:
        rect (?): ?
        color (tuple): Color of the brick.
        health (int): Value determining how many times a brick can be hit.
        alive (bool): Value determining if the brick is alive and on screen or not.

    Methods:
        hit(): Lowers the health of the brick by 1 and sets the alive attribute to false.
        draw(): Creates the image of the brick if the brick is still alive.
    """
    def __init__(self, x, y, width=60, height=20, color=(200, 50, 50), health=1):
        """
        Initializes the brick object.

        Args:
            x (int): Horizontal position of the brick.
            y (int): Vertical position of the brick.
            width (int): Width of the brick.
            height (int): Height of the brick.
            color (tuple): Color of the brick.
            health (int): Value determining how many times a brick can be hit.
        """
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.health = health
        self.alive = True

    def hit(self):
        """
        Lowers the health of the brick by 1 and sets the alive attribute to false.
        """
        self.health -= 1
        if self.health <= 0:
            self.alive = False

    def draw(self, surface):
        """
        Creates the image of the brick if the brick is still alive.

        Args:
            surface (?): ?
        """
        if self.alive:
            pygame.draw.rect(surface, self.color, self.rect)
            pygame.draw.rect(surface, (0, 0, 0), self.rect, 1)
