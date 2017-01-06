import pygame, sys, os
from pygame.locals import *

HEIGHT = 1024
WIDTH = 720
MENU = ("New Game", "Options", "About", "Exit")


class Creator(object):
    def __init__(self):
        pass

    def runMenu(self):

        pygame.init()
        # create game window
        window = pygame.display.set_mode((HEIGHT, WIDTH))

        pygame.display.set_caption('PythonGame')
        background = pygame.image.load('castle night.jpg')
        # pobieramy informacje o ekranie - tle
        screen = pygame.display.get_surface()
        # przypisanie grafiki do określonego miejsca ekranu
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

    def runAbout(self):
        while True:
            pygame.init()

            # create game window
            window = pygame.display.set_mode((HEIGHT, WIDTH))

            pygame.display.set_caption('About')
            background = pygame.image.load('castle night.jpg')
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