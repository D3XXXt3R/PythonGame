import pygame

"""Player class"""


class Player:
    def __init__(self, x_coord, y_coord):
        self.x = x_coord
        self.y = y_coord
        self.image = pygame.image.load("Game_Art/ship.png")
        self.speed = 2
        self.hit_countdown = 0
        self.timer = 0
        self.up = True
        return

    """update player position"""

    def update(self, change_x, change_y):
        self.x += (change_x * self.speed)
        self.y += (change_y * self.speed)
        return

    def change(self):
        s = pygame.Surface((20, 20))
        s.set_alpha(0)

        if self.timer == 20:  # 15 frames for UP and 15 frames for DOWN
            self.timer = 0
            self.up = not self.up

        self.timer += 1

        if self.up:
            self.hit_countdown += 1

        if self.hit_countdown % 2:
            self.image = s
        else:
            self.image = pygame.image.load("Game_Art/ship.png")
