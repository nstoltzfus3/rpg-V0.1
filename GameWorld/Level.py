import SpriteTools as st

class Level(object):

    def __init__(self, game, level):
        self.grid = np.ones((10,10))
        self.game = game
        self.level = level
        self.terrainImages = st.Terrain()
        self.itemImages = st.Items()
        self.terrainList = [self.terrainImages.grass,
                            self.terrainImages.stone,
                            self.terrainImages.water,
                            self.terrainImages.wheat,
                            self.terrainImages.tree,
                            self.terrainImages.grass_hill,

                            self.terrainImages.path_vert,
                            self.terrainImages.path_stop_up,
                            self.terrainImages.path_stop_left,
                            self.terrainImages.path_stop_right,
                            self.terrainImages.path_horiz,
                            self.terrainImages.path_bend_down_right,
                            self.terrainImages.path_t_up,
                            self.terrainImages.path_bend_down_left,
                            self.terrainImages.path_four_way,
                            self.terrainImages.path_t_left,
                            self.terrainImages.path_t_right,

                            self.terrainImages.waterland_corner_top_left
                            self.terrainImages.waterland_corner_bottom_left,
                            self.terrainImages.waterland_corner_bottom_right,
                            self.terrainImages.waterland_corner_top_right

                            self.terrainImages.landwater_top,
                            self.terrainImages.landwater_left,
                            self.terrainImages.landwater_bottom,
                            self.terrainImages.landwater_right,

                            self.terrainImages.landwater_corner_top_left,
                            self.terrainImages.landwater_corner_bottom_left,
                            self.terrainImages.landwater_corner_bottom_right,
                            self.terrainImages.landwater_corner_top_right
                            ]

        self.swordList = [self.itemImages.short_sword,
                          self.itemImages.long_sword,
                          self.itemImages.dagger,
                          self.itemImages.rapier,
                          self.itemImages.great_sword,
                          self.itemImages.pirates_sword,
                          self.itemImages.kunai,
                          self.itemImages.shuriken,
                          ]

        self.spearList = [self.itemImages.bowstaff,
                          self.itemImages.spear,
                          self.itemImages.trident,
                          self.itemImages.pirates_spear,
                          self.itemImages.halberd,
                          self.itemImages.magic_spear,
                          self.itemImages.the_reaper
                          ]

        self.axeList = [self.itemImages.mace,
                        self.itemImages.axe,
                        self.itemImages.heavy_axe,
                        self.itemImages.pirates_axe,
                        self.itemImages.war_hammer,
                        self.itemImages.magic_warhammer,
                        self.itemImages.flail]

        self.bowList = [self.itemImages.bow,
                        self.itemImages.reinforced_bow,
                        self.itemImages.cross_bow,
                        self.itemImages.long_bow,
                        self.itemImages.reinforced_longbow,
                        self.itemImages.magic_bow,
                        self.itemImages.bow_of_death
                        ]