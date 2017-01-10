import pygame


class Enemy:
    def __init__(self, x_coord, y_coord):
        self.x = x_coord
        self.y = y_coord
        self.image = pygame.image.load('Game_Art/enemy.png')
        self.speed = 3
        return

    def update(self, surface, dirx, y_amount=0):
        self.x += (dirx * self.speed)
        self.y += y_amount
        surface.blit(self.image, (self.x, self.y))
        return
