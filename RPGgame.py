import sys, pygame as pg
import SpriteTools
from GameWorld import GameWorld as gw
import time

def init_surface():
    pg.init()
    size = width, height = 320, 320
    screen = pg.display.set_mode(size)
    return screen

def draw_map(game_world, surface):
    for i in range(game_world.grid.shape[0]):
        for j in range(game_world.grid.shape[1]):
            terrainImage = game_world.terrainList[int(game_world.grid[i, j])]
            terrainRect = terrainImage.get_rect()
            terrainRect = terrainRect.move([i*32,j*32])
            surface.blit(terrainImage, terrainRect)
            pg.display.update()

screen = init_surface()
Game = gw.GameWorld(10,screen)
Game.init_outer_walls()
draw_map(Game, screen)


while 1:

    for event in pg.event.get():
        if event.type == pg.QUIT: sys.exit()
        if event.type == pg.KEYDOWN:
            print(event)
            print(event.key)
    # ballrect = ballrect.move(speed)
    # if ballrect.left < 0 or ballrect.right > width:
    #     speed[0] = -speed[0]
    # if ballrect.top < 0 or ballrect.bottom > height:
    #     speed[1] = -speed[1]

    # screen.fill(black)
    # screen.blit(short_sword, ballrect)
    pg.display.flip()

    time.sleep(1)