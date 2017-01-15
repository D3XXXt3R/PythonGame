import pygame

"""enemy class"""


class Enemy:
    def __init__(self, image, x_coord, y_coord, points, speed):
        self.x = x_coord
        self.y = y_coord
        self.image = pygame.image.load('Game_Art/'+image+'.png')
        self.speed = speed
        self.points = points  # enemy value
        return

    """update enemy position"""

    def update(self, surface, dirx, y_amount=0):
        self.x += (dirx * self.speed)
        self.y += y_amount
        surface.blit(self.image, (self.x, self.y))
        return
