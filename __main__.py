import os

from Creator import *


class MainMenu(object):

    def __init__(self):
        pass

    def run(self):
        cr = Creator()
        cr.run_menu()

if __name__ == "__main__":

    X = 100
    Y = 30

    # set window
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (X, Y)
    MM = MainMenu()
    MM.run()
