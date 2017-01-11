import random

import pygame, sys, os
from pygame.locals import *
from Bullet import *
from Enemy import *
from EnemyBullet import EnemyBullet

HEIGHT = 720
WIDTH = 1024
MENU = ("New Game", "Options", "About", "Exit")
SCORE = 0  # here we count score
LIFE = 3  # player life


class Creator(object):
    def __init__(self, score=SCORE, life=LIFE):
        self.score = score
        self.enemies_bullets = []
        self.life = life

    """generate enemy"""

    def generate_enemies(self):
        matrix = []
        for y in range(5):
            if y == 0:
                points = 30
            elif y == 1 or y == 2:
                points = 20
            else:
                points = 10
            enemies = [Enemy(80 + (50 * x), 50 + (60 * y), points) for x in range(11)]
            matrix.append(enemies)
        return matrix

    def check_collision(self, object1_x, object1_y, object2_x, object2_y):
        return (
            (object1_x > object2_x) and (object1_x < object2_x+100) and
            (object1_y > object2_y) and (object1_y < object2_y+100)
        )

    def run_menu(self):

        pygame.init()
        # create game window
        window = pygame.display.set_mode((WIDTH, HEIGHT))

        pygame.display.set_caption('PythonGame')
        background = pygame.image.load('Game_Art/castle night.jpg')
        file = 'Game_Art/nebula.mp3'
        pygame.mixer.init()
        pygame.mixer.music.load(file)
        pygame.mixer.music.play()
        screen = pygame.display.get_surface()
        screen.blit(background, (0, 0))

        i = 0
        while i < len(MENU):
            myfont = pygame.font.SysFont("Comic Sans MS", 40)
            textsurface = myfont.render(MENU[i], False, (150, 120, 232))
            height = 150 + (i * 200)
            width = 50 + (i * 200)
            screen.blit(textsurface, (height, width))
            pygame.display.flip()
            i += 1

        # main loop
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    sys.exit(0)
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        sys.exit(0)
                if event.type == MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = event.pos
                    if 151 < mouse_x < 346 and 62 < mouse_y < 95:
                        import NewGame as ng
                        ng.NewGame.run(self)
                        print("New Game")
                    elif 352 < mouse_x < 492 and 261 < mouse_y < 304:
                        print("Options")
                    elif 552 < mouse_x < 662 and 464 < mouse_y < 494:
                        import About as ab
                        ab.About.run(self)
                        print("About")
                    elif 750 < mouse_x < 828 and 665 < mouse_y < 696:
                        sys.exit(0)
                        print("Exit")
                if event.type == MOUSEMOTION:
                    mouse_x, mouse_y = event.pos
                    if 151 < mouse_x < 346 and 62 < mouse_y < 95:
                        textsurface = myfont.render("New Game", False, (255, 255, 255))
                        screen.blit(textsurface, (150, 50))
                        pygame.display.flip()
                    else:
                        textsurface = myfont.render("New Game", False, (150, 120, 232))
                        screen.blit(textsurface, (150, 50))
                        pygame.display.flip()
                    if 352 < mouse_x < 492 and 261 < mouse_y < 304:
                        textsurface = myfont.render("Options", False, (255, 255, 255))
                        screen.blit(textsurface, (351, 251))
                        pygame.display.flip()
                    else:
                        textsurface = myfont.render("Options", False, (150, 120, 232))
                        screen.blit(textsurface, (351, 251))
                        pygame.display.flip()
                    if 552 < mouse_x < 662 and 464 < mouse_y < 494:
                        textsurface = myfont.render("About", False, (255, 255, 255))
                        screen.blit(textsurface, (551, 451))
                        pygame.display.flip()
                    else:
                        textsurface = myfont.render("About", False, (150, 120, 232))
                        screen.blit(textsurface, (551, 451))
                        pygame.display.flip()
                    if 750 < mouse_x < 828 and 665 < mouse_y < 696:
                        textsurface = myfont.render("Exit", False, (255, 255, 255))
                        screen.blit(textsurface, (751, 651))
                        pygame.display.flip()
                    else:
                        textsurface = myfont.render("Exit", False, (150, 120, 232))
                        screen.blit(textsurface, (751, 651))
                        pygame.display.flip()
                        # print(str(mouse_x) + " " + str(mouse_y))

    def run_about(self):
        while True:
            pygame.init()

            # create game window
            window = pygame.display.set_mode((WIDTH, HEIGHT))

            pygame.display.set_caption('About')
            background = pygame.image.load('Game_Art/castle night.jpg')
            # pobieramy informacje o ekranie - tle
            screen = pygame.display.get_surface()
            # przypisanie grafiki do określonego miejsca ekranu
            screen.blit(background, (0, 0))

            myfont = pygame.font.SysFont("Comic Sans MS", 30)
            author = myfont.render("Author: D3XXXt3r", False, (150, 120, 232))
            screen.blit(author, (150, 250))
            github = myfont.render("Github: https://github.com/D3XXXt3R/PythonGame", False, (150, 120, 232))
            screen.blit(github, (150, 300))
            github = myfont.render("Version: 1.0", False, (150, 120, 232))
            screen.blit(github, (150, 350))
            back = myfont.render("Back", False, (150, 120, 232))
            screen.blit(back, (150, 400))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == QUIT:
                    sys.exit(0)
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        sys.exit(0)
                if event.type == MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = event.pos
                    if 152 < mouse_x < 214 and 407 < mouse_y < 438:
                        import __main__ as mm
                        mm.MainMenu.run(self)
                if event.type == MOUSEMOTION:
                    mouse_x, mouse_y = event.pos
                    if 152 < mouse_x < 214 and 407 < mouse_y < 438:
                        back = myfont.render("Back", False, (255, 255, 255))
                        screen.blit(back, (150, 400))
                        pygame.display.flip()

    def run_new_game(self):

        pygame.init()
        enemy_can_shoot = True
        enemy_fire_wait = 1500
        bullets_array = []
        enemies_matrix = self.generate_enemies()
        can_shoot = True
        fire_wait = 500

        player_x = 400
        player_y = 650

        moving = False

        # create game window
        screen = pygame.display.set_mode((WIDTH, HEIGHT))

        pygame.display.set_caption('New Game')
        background = pygame.image.load('Game_Art/castle night.jpg')
        player = pygame.image.load("Game_Art/ship.png")
        myfont = pygame.font.SysFont("Comic Sans MS", 30)
        back = myfont.render("Back", False, (150, 120, 232))
        screen.blit(back, (150, 400))

        change_x = 0
        change_y = 0

        # pygame.display.flip()
        while True:
            fire_wait -= CLOCK.tick(60)
            enemy_fire_wait -= CLOCK.tick(60)
            for event in pygame.event.get():
                if event.type == QUIT:
                    sys.exit(0)
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        sys.exit(0)
                    elif event.key == K_LEFT:
                        change_x = -5
                    elif event.key == K_RIGHT:
                        change_x = 5
                    elif event.key == K_UP:
                        change_y = -5
                    elif event.key == K_DOWN:
                        change_y = 5
                    elif event.key == K_SPACE:
                        bullet = Bullet(screen, player_x, player_y)
                        bullets_array.append(bullet)
                        can_shoot = False

                    if not can_shoot and fire_wait <= 0:
                        can_shoot = True
                        fire_wait = 500

                if event.type == MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = event.pos
                    if 152 < mouse_x < 214 and 407 < mouse_y < 438:
                        import __main__ as mm
                        mm.MainMenu.run(self)
                if event.type == MOUSEMOTION:
                    mouse_x, mouse_y = event.pos
                    if 152 < mouse_x < 214 and 407 < mouse_y < 438:
                        back = myfont.render("Back", False, (255, 255, 255))
                        screen.blit(back, (150, 400))
                        pygame.display.flip()

            player_x += change_x
            player_y += change_y

            if 0 > player_x:
                player_x = 0
            elif player_x > WIDTH - 50:
                player_x = WIDTH - 50
            if 0 > player_y:
                player_y = 0
            elif player_y > HEIGHT - 50:
                player_y = HEIGHT - 50

            screen.blit(background, (0, 0))
            screen.blit(player, (player_x, player_y))
            score_label = myfont.render("Score: {}".format(self.score), 1, (255, 0, 0))
            screen.blit(score_label, (25, 575))

            life_label = myfont.render("Life: {}".format(self.life), 1, (255, 0, 0))
            screen.blit(life_label, (750, 575))

            # loop where we update enemy move
            for enemies in enemies_matrix:
                for enemy in enemies:
                    if enemies[-1].x > 990:
                        dirx = -1
                        moving = True
                        enemy.update(screen, 0, 5)
                    elif enemies[0].x < 0:
                        dirx = 1
                        moving = True
                        enemy.update(screen, 0, 5)
                    elif not moving:
                        dirx = 1
                    enemy.update(screen, dirx)

            if enemy_can_shoot:
                flat_list = [enemy for enemies in enemies_matrix for enemy in enemies]
                random_enemy = random.choice(flat_list)
                enemy_bullet = EnemyBullet(screen, random_enemy.x, random_enemy.y)
                self.enemies_bullets.append(enemy_bullet)
                enemy_can_shoot = False

            if not enemy_can_shoot and enemy_fire_wait <= 0:
                enemy_fire_wait = 1500
                enemy_can_shoot = True

            for enemy_bullet in self.enemies_bullets:
                enemy_bullet.update()
                if enemy_bullet.x > 990:
                    self.enemies_bullets.remove(enemy_bullet)

                if self.check_collision(enemy_bullet.x, enemy_bullet.y, player_x,
                                        player_y) and enemy_bullet in self.enemies_bullets:
                    self.enemies_bullets.remove(enemy_bullet)
                    self.life -= 1

            for bullet in bullets_array:
                bullet.update()
                if bullet.y < 0:
                    bullets_array.remove(bullet)
                for enemies in enemies_matrix:
                    for enemy in enemies:
                        if (self.check_collision(bullet.x, bullet.y, enemy.x, enemy.y)
                            and bullet in bullets_array):
                            self.score += enemy.points
                            enemies.remove(enemy)
                            bullets_array.remove(bullet)

            pygame.display.update()
