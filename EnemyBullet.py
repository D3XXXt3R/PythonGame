import pygame

"""Enemy Bullet Class"""


class EnemyBullet:
    def __init__(self, surface, x_coord, y_coord):
        self.surface = surface
        self.x = x_coord + 12
        self.y = y_coord
        self.image = pygame.image.load('Game_Art/laser.png')
        return

    def update(self, y_amount):
        self.y += y_amount
        self.surface.blit(self.image, (self.x, self.y))
        return
