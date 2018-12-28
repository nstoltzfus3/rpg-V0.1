import numpy as np
from enum import Enum
from pygame import *

class Terrain(Enum):
    BLANK = 0
    PLAIN = 1
    GRASS = 2
    MOUNT = 3
    WALL = 4
    UNIT = 5

class GameWorld(object):
    """
    GameWorld class holds an instance of a singular running game
    """
    def __init__(self, size):
        self.grid = np.zeros((10,10))

    def toString(self):
        for row in self.grid:
            for element in row:
                print(str(int(element)).strip('.') + " ", end="")
            print("")

    def initOuterWalls(self):
        height, width = self.grid.shape

        self.grid[0,:] = 4
        self.grid[height - 1,:] = 4
        self.grid[:,0] = 4
        self.grid[:,width - 1] = 4

    def initBasicGame(self):
        self.initOuterWalls()

