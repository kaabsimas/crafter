import pygame as pg
import random
from settings import *
from pygame import *

class Map:
    def __init__(self):
        self.data = []
        size = 20
        for x in range(0, size):
            row = []
            for y in range(0, size):
                row.append(random.randint(0, 15))
            self.data.append(row)
        self.width = size * TILEWIDTH
        self.height = size * TILEHEIGHT
        self.image = pg.Surface((size * TILEWIDTH, size * TILEHEIGHT + 10))
        self.rect  = self.image.get_rect()
        self.rect.midtop = (WIDTH/2, 50)

class Camera:
    def __init__(self, width, height):
        self.camera = pg.Rect(0, 0, width, height)
        self.width  = width
        self.height = height

    def apply(self, entity):
        return entity.rect.move(self.camera.topleft)

    def update(self, target):
        x = -target.rect.x + int(WIDTH / 2)
        y = -target.rect.y + int(HEIGHT / 2)
        self.camera = pg.Rect(x, y, self.width, self.height)
