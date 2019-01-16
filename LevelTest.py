import sys, pygame as pg
from GameWorld import Level as lv

def init_surface():
    pg.init()
    size = width, height = 320, 320
    screen = pg.display.set_mode(size)
    return screen

def draw_map(level, surface):
    for i in range(level.size):
        for j in range(level.size):
            # terrainImage = game_world.terrainList[int(game_world.grid[i, j])]
            terrainImage = level.grid[i*level.size+j]
            terrainRect = terrainImage.get_rect()
            terrainRect = terrainRect.move([i*32,j*32])
            surface.blit(terrainImage, terrainRect)
            pg.display.update()

screen = init_surface()
Level = lv.Level(10, screen, 1)
draw_map(Level, screen)


while 1:

    for event in pg.event.get():
        if event.type == pg.QUIT: sys.exit()
        if event.type == pg.KEYDOWN:
            print(event)
            print(event.key)

    pg.display.flip()