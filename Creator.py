import random
import time

import pygame, sys, os
from pygame.locals import *

from Bonus import Bonus
from Bullet import *
from Enemy import *
from EnemyBullet import EnemyBullet
from Player import Player

HEIGHT = 720
WIDTH = 1024
MENU = ("New Game", "Options", "About", "Exit")
SCORE = 0  # here we count score
LIFE = 200  # player life
ORANGE = (181, 131, 45)
LEVELS = ("level1", "level2", "level3")
ENEMIES = ("enemy", "red")
BONUS = ("Life", "Shield")


class Creator(object):
    def __init__(self, score=SCORE, life=LIFE):
        self.score = score
        self.enemies_bullets = []
        self.screen = pygame.display.get_surface()
        self.life = life
        self.player_hit = 0
        self.change_x = 0
        self.change_y = 0
        self.level = 0
        self.enemy_level = 0
        self.enemy_speed = 3
        self.bonus = 0

    def generate_random_coordinates(self):
        return random.randrange(40, WIDTH - 40)

    def generate_random_bonus(self):
        return random.randrange(0, 2)

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
            enemies = [Enemy(ENEMIES[self.enemy_level], 80 + (50 * x), 50 + (60 * y), points, self.enemy_speed) for x in
                       range(11)]
            matrix.append(enemies)
        return matrix

    def check_collision(self, object1_x, object1_y, object2_x, object2_y):
        # return (
        #     (object1_x > object2_x) and (object1_x < object2_x + 20) and
        #     (object1_y > object2_y) and (object1_y < object2_y)
        # )
        if self.player_hit <= 0:
            if object2_x - 35 < object1_x < object2_x + 35 and (object1_y > object2_y) and (object1_y < object2_y + 35):
                return True

    def game_over_screen(self):
        time.sleep(2)
        myfont = pygame.font.Font(None, 15)
        background = pygame.image.load('Game_Art/falling.png')
        label = myfont.render("Press Y to restart game, N to exit", 1, (255, 0, 0))
        score = myfont.render("You finished with score: {}".format(self.score), 1, (255, 0, 0))
        self.screen.fill((0, 0, 0))
        self.screen.blit(background, (0, 0))
        self.screen.blit(label, (100, 100))
        self.screen.blit(score, (100, 120))
        file = 'Game_Art/Space.flac'
        pygame.mixer.init()
        pygame.mixer.music.load(file)
        pygame.mixer.music.play()
        pygame.display.flip()
        while True:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_RETURN:
                        self.run_new_game()
                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE) or (
                                event.type == KEYDOWN and event.key == K_n):
                    exit()

    def continue_screen(self):
        myfont = pygame.font.Font(None, 15)
        label = myfont.render("Press ENTER to continue game", 1, (255, 0, 0))
        score = myfont.render("Your score: {}".format(self.score), 1, (255, 0, 0))
        self.screen.fill((0, 0, 0))
        self.screen.blit(label, (100, 100))
        self.screen.blit(score, (100, 120))
        pygame.display.flip()
        while True:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_RETURN or event.key == K_y:
                        self.level += 1
                        self.enemy_level += 1
                        self.enemy_speed += 1
                        self.run_new_game()
                if (event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE) or (
                                event.type == KEYDOWN and event.key == K_n)):
                    exit()

    def run_menu(self):

        pygame.init()
        # create game window
        window = pygame.display.set_mode((WIDTH, HEIGHT))

        pygame.display.set_caption('PythonGame')
        background = pygame.image.load('Game_Art/Background-3.png')
        file = 'Game_Art/Space Atmosphere.mp3'
        pygame.mixer.init()
        pygame.mixer.music.load(file)
        pygame.mixer.music.play()
        screen = pygame.display.get_surface()
        screen.blit(background, (0, 0))

        i = 0
        while i < len(MENU):
            myfont = pygame.font.Font("Game_Art/font.ttf", 40)
            textsurface = myfont.render(MENU[i], False, ORANGE)
            height = 150 + (i * 100)
            width = 400
            print(height)
            screen.blit(textsurface, (width, height))
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
                    if 400 < mouse_x < 630 and 170 < mouse_y < 210:
                        import NewGame as ng
                        ng.NewGame.run(self)
                        print("New Game")
                    elif 400 < mouse_x < 590 and 270 < mouse_y < 310:
                        print("Options")
                    elif 400 < mouse_x < 530 and 370 < mouse_y < 410:
                        import About as ab
                        ab.About.run(self)
                        print("About")
                    elif 400 < mouse_x < 500 and 470 < mouse_y < 510:
                        sys.exit(0)
                        print("Exit")
                if event.type == MOUSEMOTION:
                    mouse_x, mouse_y = event.pos
                    if 400 < mouse_x < 630 and 170 < mouse_y < 210:
                        textsurface = myfont.render("New Game", False, (255, 255, 255))
                        screen.blit(textsurface, (400, 150))
                        pygame.display.flip()
                    else:
                        textsurface = myfont.render("New Game", False, ORANGE)
                        screen.blit(textsurface, (400, 150))
                        pygame.display.flip()
                    if 400 < mouse_x < 590 and 270 < mouse_y < 310:
                        textsurface = myfont.render("Options", False, (255, 255, 255))
                        screen.blit(textsurface, (400, 250))
                        pygame.display.flip()
                    else:
                        textsurface = myfont.render("Options", False, ORANGE)
                        screen.blit(textsurface, (400, 250))
                        pygame.display.flip()
                    if 400 < mouse_x < 530 and 370 < mouse_y < 410:
                        textsurface = myfont.render("About", False, (255, 255, 255))
                        screen.blit(textsurface, (400, 350))
                        pygame.display.flip()
                    else:
                        textsurface = myfont.render("About", False, ORANGE)
                        screen.blit(textsurface, (400, 350))
                        pygame.display.flip()
                    if 400 < mouse_x < 500 and 470 < mouse_y < 510:
                        textsurface = myfont.render("Exit", False, (255, 255, 255))
                        screen.blit(textsurface, (400, 450))
                        pygame.display.flip()
                    else:
                        textsurface = myfont.render("Exit", False, ORANGE)
                        screen.blit(textsurface, (400, 450))
                        pygame.display.flip()
                        # print(str(mouse_x) + " " + str(mouse_y))

    def run_about(self):
        while True:
            pygame.init()

            # create game window
            window = pygame.display.set_mode((WIDTH, HEIGHT))

            pygame.display.set_caption('About')
            background = pygame.image.load('Game_Art/Background-3.png')
            # pobieramy informacje o ekranie - tle
            screen = pygame.display.get_surface()
            # przypisanie grafiki do określonego miejsca ekranu
            screen.blit(background, (0, 0))

            myfont = pygame.font.Font("Game_Art/font.ttf", 28)
            author = myfont.render("Author: D3XXXt3r", False, ORANGE)
            screen.blit(author, (150, 250))
            github = myfont.render("Github: https://github.com/D3XXXt3R/PythonGame", False, ORANGE)
            screen.blit(github, (150, 300))
            github = myfont.render("Version: 1.0", False, ORANGE)
            screen.blit(github, (150, 350))
            back = myfont.render("Back", False, ORANGE)
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
        bonus_array = []
        enemies_matrix = self.generate_enemies()
        can_shoot = True
        fire_wait = 500
        bonus_wait = 500
        loop = True

        moving = False

        # create game window
        screen = pygame.display.set_mode((WIDTH, HEIGHT))

        pygame.display.set_caption('New Game')
        background = pygame.image.load('Game_Art/levels/' + LEVELS[self.level] + '.png')
        player = Player(400, 650)  # create player class object

        myfont = pygame.font.SysFont("Comic Sans MS", 30)

        while loop:

            fire_wait -= CLOCK.tick(60)
            enemy_fire_wait -= CLOCK.tick(60)
            bonus_wait -= CLOCK.tick(60)
            self.player_hit -= CLOCK.tick(60)
            for event in pygame.event.get():
                if event.type == QUIT:
                    sys.exit(0)
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        sys.exit(0)
                    elif event.key == K_LEFT:
                        self.change_x = -5
                    elif event.key == K_RIGHT:
                        self.change_x = 5
                    elif event.key == K_UP:
                        self.change_y = -5
                    elif event.key == K_DOWN:
                        self.change_y = 5
                    elif event.key == K_SPACE:
                        file = 'Game_Art/playerLaser.wav'
                        pygame.mixer.init()
                        pygame.mixer.music.load(file)
                        pygame.mixer.music.play()
                        bullet = Bullet(screen, player.x, player.y)
                        bullets_array.append(bullet)
                        can_shoot = False

                    if not can_shoot and fire_wait <= 0:
                        can_shoot = True
                        fire_wait = 500

                if not self.life:
                    loop = False
                    self.game_over_screen()

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

            player.update(self.change_x, self.change_y)

            if 0 > player.x:
                player.x = 0
            elif player.x > WIDTH - 50:
                player.x = WIDTH - 50
            if 0 > player.y:
                player.y = 0
            elif player.y > HEIGHT - 50:
                player.y = HEIGHT - 50

            screen.blit(background, (0, 0))
            screen.blit(player.image, (player.x, player.y))
            score_label = myfont.render("Score: {}".format(self.score), 1, (255, 0, 0))
            screen.blit(score_label, (25, 575))
            if self.player_hit > 0:
                player.change()
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
                    if self.check_collision(player.x, player.y, enemy.x, enemy.y):
                        file = 'Game_Art/explosion1.mp3'
                        pygame.mixer.init()
                        pygame.mixer.music.load(file)
                        pygame.mixer.music.play()
                        self.player_hit = 2000
                        self.life -= 1
                    enemy.update(screen, dirx)

            if enemy_can_shoot:
                file = 'Game_Art/laser1.flac'
                pygame.mixer.init()
                pygame.mixer.music.load(file)
                pygame.mixer.music.play()
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

                if self.check_collision(enemy_bullet.x, enemy_bullet.y, player.x,
                                        player.y) and enemy_bullet in self.enemies_bullets:
                    file = 'Game_Art/explosion1.mp3'
                    pygame.mixer.init()
                    pygame.mixer.music.load(file)
                    pygame.mixer.music.play()
                    self.player_hit = 2000
                    self.enemies_bullets.remove(enemy_bullet)
                    self.life -= 1
                    # time.sleep(5)

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

            if bonus_wait < 0:
                bonus_number = self.generate_random_bonus()
                bonus = Bonus(self.screen, self.generate_random_coordinates(), 1, BONUS[bonus_number])
                bonus_array.append(bonus)
                bonus_wait = 500

            for bonus in bonus_array:
                bonus.update()
                if bonus.y < 0:
                    bonus_array.remove(bonus)
                if self.check_collision(bonus.x, bonus.y, player.x, player.y):
                    file = 'Game_Art/Bonus.wav'
                    pygame.mixer.init()
                    pygame.mixer.music.load(file)
                    pygame.mixer.music.play()
                    self.life += 1

            if not any(enemies_matrix):
                self.continue_screen()

            pygame.display.update()
