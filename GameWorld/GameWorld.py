import numpy as np
from enum import Enum
from pygame import *
import SpriteTools as st

class Terrain(Enum):
    PLAIN = 0
    GRASS = 1
    MOUNT = 2
    water = 3

class GameWorld(object):
    """
    GameWorld class holds an instance of a singular running game
    """
    def __init__(self, size, surface):

        self.grid = np.ones((10,10))
        self.size = size
        self.surface = surface
        self.terrainImages = st.Terrain()
        self.itemImages = st.Items()
        self.terrainList = [self.terrainImages.wheat,
                            self.terrainImages.grass,
                            self.terrainImages.grass_hill,
                            self.terrainImages.water,

                            self.terrainImages.landwater_top,
                            self.terrainImages.landwater_left,
                            self.terrainImages.landwater_bottom,
                            self.terrainImages.landwater_right,

                            self.terrainImages.waterland_corner_top_left,
                            self.terrainImages.waterland_corner_bottom_left,
                            self.terrainImages.waterland_corner_bottom_right,
                            self.terrainImages.waterland_corner_top_right]

    def __str__(self):
        out = "----------------------\n"
        for row in self.grid:
            for element in row:
                out = out + str(int(element)).strip('.') + " "
            out = out + "\n"
        return out

    def init_outer_walls(self):
        height, width = self.grid.shape
        self.grid[0,1:-1] = 7
        self.grid[height - 1,1:-1] = 5
        self.grid[1:-1,0] = 6
        self.grid[1:-1,width - 1] = 4

        self.grid[0,0] = 8
        self.grid[height - 1,0] = 11
        self.grid[0,width - 1] = 9
        self.grid[height - 1,width - 1] = 10


    def init_basic_game(self):
        self.init_outer_walls()


