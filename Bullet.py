import pygame

CLOCK = pygame.time.Clock()

# klasa pocisku
class Bullet:

    def __init__(self, surface, x_coord, y_coord):
        self.surface = surface
        self.x = x_coord + 24
        self.y = y_coord
        self.image = pygame.image.load('Game_art/bullet.png')
        return

    def update(self, y_amount=5):
        self.y -= y_amount
        self.surface.blit(self.image, (self.x, self.y))
        return