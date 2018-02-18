import pygame as pg

class Map:
    def __init__(self, size):
        self.width  = size[0]
        self.height = size[1]
        self.image  = pg.Surface(size)
        self.rect   = self.image.get_rect()
        self.data   = []
        # size = 20
        # for x in range(0, size):
        #     row = []
        #     for y in range(0, size):
        #         row.append(random.randint(0, 15))
        #     self.data.append(row)
        # self.width = size * TILEWIDTH
        # self.height = size * TILEHEIGHT
        # self.image = pg.Surface((size * TILEWIDTH, size * TILEHEIGHT + 10))
        # self.rect  = self.image.get_rect()
        # self.rect.midtop = (WIDTH/2, 50)

    def set_data(self, data):
        self.data = data

    def get_data(self):
        return self.data

    def set_width(self, width):
        self.width = width
        self.image  = pg.Surface((self.width, self.height))
        self.rect   = self.image.get_rect()

    def set_height(self, height):
        self.height = height
        self.image  = pg.Surface((self.width, self.height))
        self.rect   = self.image.get_rect()

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height
    
    def make(self):
        pass
