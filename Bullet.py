import pygame

CLOCK = pygame.time.Clock()


class Bullet:
    def __init__(self, surface, x_coord, y_coord):
        self.surface = surface
        self.x = x_coord - 32
        self.y = y_coord - 70
        self.image = pygame.image.load('Game_art/bullet.png')
        return

    def update(self, y_amount=5):
        self.y -= y_amount
        self.surface.blit(self.image, (self.x, self.y))
        return
