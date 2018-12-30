import pygame as pg
def get_image(posx, posy, width, height, sprite_sheet):
    """Extracts image from sprite sheet"""
    image = pg.Surface([width, height])
    image.blit(sprite_sheet, (0, 0), (posx, posy, width, height))
  #  image.set_colorkey(c.BLACK)

    return image

class Items():

    def __init__(self):
        items = pg.image.load("sprites/items.png")
        blue_units = pg.image.load("sprites/units_blue.png")
        red_units = pg.image.load("sprites/units_blue.png")

        # load swords, save in memory
        self.short_sword = get_image(0,0,32,32,items)
        self.long_sword = get_image(1,0,32,32,items)
        self.dagger = get_image(2,0,32,32,items)
        self.rapier = get_image(3,0,32,32,items)
        self.great_sword = get_image(4,0,32,32,items)
        self.pirates_sword = get_image(5,0,32,32,items)
        self.kunai = get_image(6,0,32,32,items)
        self.shuriken = get_image(7,0,32,32,items)

        # load spears
        self.bowstaff = get_image(0,1,32,32,items)
        self.spear = get_image(1,1,32,32,items)
        self.trident = get_image(2,1,32,32,items)
        self.pirates_spear = get_image(3,1,32,32,items)
        self.halberd = get_image(4,1,32,32,items)
        self.magic_spear = get_image(5,1,32,32,items)
        self.the_reaper = get_image(6,1,32,32,items)

        #load axes
        self.mace = get_image(0,2,32,32,items)
        self.axe = get_image(1,1,32,32,items)
        self.heavy_axe = get_image(2,1,32,32,items)
        self.pirates_axe = get_image(3,1,32,32,items)
        self.war_hammer = get_image(4,1,32,32,items)
        self.magic_warhammer = get_image(5,1,32,32,items)
        self.flail = get_image(6,1,32,32,items)

        # load bows
        self.bow = get_image(0, 3, 32, 32, items)
        self.reinforced_bow = get_image(1, 3, 32, 32, items)
        self.cross_bow = get_image(2, 3, 32, 32, items)
        self.long_bow = get_image(3, 3, 32, 32, items)
        self.reinforced_bow = get_image(4, 3, 32, 32, items)
        self.reinforced_longbow= get_image(5, 3, 32, 32, items)
        self.magic_bow = get_image(6, 3, 32, 32, items)
        self.bow_of_death = get_image(7, 3, 32, 32, items)



class Terrain():
    """
    class to hold the different sprites taken from the terrain pallet
    """
    def __init__(self):
        terrain = pg.image.load("sprites/terrain.png")

        # load terrain
        self.grass = get_image(0, 0, 32, 32, terrain)
        self.stone = get_image(1 * 32, 0, 32, 32, terrain)
        self.water = get_image(2 * 32, 0, 32, 32, terrain)
        self.wheat = get_image(3 * 32, 0, 32, 32, terrain)
        self.path_vert = get_image(4* 32, 0, 32, 32, terrain)
        self.path_stop_up = get_image(5* 32, 0, 32, 32, terrain)
        self.path_horiz = get_image(6* 32, 0, 32, 32, terrain)
        self.path_bend_down_right = get_image(7* 32, 0, 32, 32, terrain)
        self.path_t_up = get_image(8* 32, 0, 32, 32, terrain)
        self.path_bend_down_left = get_image(9* 32, 0, 32, 32, terrain)

        self.tree = get_image(0, 1* 32, 32, 32, terrain)
        self.grass_hill = get_image(1* 32, 1* 32, 32, 32, terrain)
        self.path_stop_left = get_image(4* 32, 1* 32, 32, 32, terrain)
        self.path_four_way = get_image(5* 32, 1* 32, 32, 32, terrain)
        self.path_stop_right = get_image(6* 32, 1* 32, 32, 32, terrain)
        self.path_t_left = get_image(7* 32, 1* 32, 32, 32, terrain)
        self.path_t_right= get_image(9* 32, 1* 32, 32, 32, terrain)

        # load water terrain
        self.waterland_corner_top_left = get_image(5 * 32, 3 * 32, 32, 32, terrain)
        self.waterland_corner_bottom_left = get_image(5 * 32, 4 * 32, 32, 32, terrain)
        self.waterland_corner_top_right = get_image(6 * 32, 3 * 32, 32, 32, terrain)
        self.waterland_corner_bottom_right = get_image(6 * 32, 4 * 32, 32, 32, terrain)

        self.landwater_corner_top_left = get_image(7 * 32, 3 * 32, 32, 32, terrain)
        self.landwater_corner_bottom_left = get_image(7 * 32, 5 * 32, 32, 32, terrain)
        self.landwater_corner_top_right = get_image(9 * 32, 3 * 32, 32, 32, terrain)
        self.landwater_corner_bottom_right = get_image(9 * 32, 5 * 32, 32, 32, terrain)

        self.landwater_top = get_image(8 * 32, 3 * 32, 32, 32, terrain)
        self.landwater_bottom = get_image(8 * 32, 5 * 32, 32, 32, terrain)
        self.landwater_left = get_image(7 * 32, 4 * 32, 32, 32, terrain)
        self.landwater_right = get_image(9 * 32, 4 * 32, 32, 32, terrain)









