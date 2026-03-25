import pygame

class BRICK:
    def __init__(self, x, y, width=60, height=20, color=(200, 50, 50), health=1):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.health = health
        self.alive = True

    def hit(self):
        """

        """
        self.health -= 1
        if self.health <= 0:
            self.alive = False

    def draw(self, surface):
        """
        Description

        Args:
            surface:
        """
        if self.alive:
            pygame.draw.rect(surface, self.color, self.rect)
            pygame.draw.rect(surface, (0, 0, 0), self.rect, 1)
