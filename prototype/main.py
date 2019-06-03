# -*- coding: latin-1 -*-
# KidsCanCode - Game Development with Pygame video series
# Tile-based game - Part 1
# Project setup
# Video link: https://youtu.be/3UxnelT9aCo
import pygame as pg
import os
import sys
from settings import *
from sprites import *
from pygame.locals import *
from tilemap import *

def load_image( name, colorkey=None):
    fullname = os.path.join('../assets', name)
    try:
        image = pg.image.load(fullname)
    except pg.error, message:
        print 'Não dá pra carregar: ', name
        raise SystemExit, message
    image = image.convert()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image, image.get_rect()

class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        pg.key.set_repeat(500, 100)
        self.load_data()

    def load_data(self):
        self.tilesSrc, self.tilesRect = load_image('isometric_new_tiles_by_spasquini.png', -1)
        self.map    = Map()

    def new(self):
        # initialize all variables and do all the setup for a new game
        self.all_sprites = pg.sprite.Group()
        self.tiles       = pg.sprite.Group()
        # self.walls = pg.sprite.Group()
        self.player = Player(self, 0, 0)
        self.camera = Camera(self.map.width, self.map.height)
        self.draw_grid()

    def run(self):
        # game loop - set self.playing = False to end the game
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
            self.events()
            self.update()
            self.draw()

    def quit(self):
        pg.quit()
        sys.exit()

    def update(self):
        # update portion of the game loop
        self.all_sprites.update()
        self.camera.update(self.player)

    def draw_grid(self):
        for x, row in enumerate(self.map.data):
            for y, index in enumerate(row):
                aux = Tile(self, index, x, y)
                self.map.image.blit(aux.image, self.camera.apply(aux))
                # pg.draw.polygon(self.screen, 0x115, ((aux.rect.x, aux.rect.y),(TILEWIDTH, aux.rect.y),(TILEWIDTH, TILEHEIGHT), (aux.rect.x, TILEHEIGHT)), 1)
                # origin = (((x-y)*TILEWIDTH/2) + WIDTH/2, ((x+y)*TILEHEIGHT/2) + 50 + ( 5 if index < 4 else 0))
                # area = ( index * TILEWIDTH, 0, TILEWIDTH, tilesRect[3] )
                # dest = ( origin[0] + (-TILEWIDTH / 2), origin[1], origin[0]+TILEWIDTH, origin[1]+tilesRect[3] )
                # self.screen.blit(tiles, dest, area)

    def draw(self):
        self.screen.fill(BGCOLOR)
        # self.draw_grid()
        self.screen.blit(self.map.image, self.camera.apply(self.map))
        self.screen.blit(self.player.image, self.camera.apply(self.player))
        pg.display.flip()

    def events(self):
        # catch all events here
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.quit()
                if event.key == pg.K_LEFT:
                    if(self.player.x > 0):
                        self.player.move(dx=-1)
                if event.key == pg.K_RIGHT:
                    if(self.player.x < len(self.map.data[0])-1):
                        self.player.move(dx=1)
                if event.key == pg.K_UP:
                    if(self.player.y > 0):
                        self.player.move(dy=-1)
                if event.key == pg.K_DOWN:
                    if(self.player.y < len(self.map.data)-1):
                        self.player.move(dy=1)

    def show_start_screen(self):
        pass

    def show_go_screen(self):
        pass

# create the game object
g = Game()
g.show_start_screen()
while True:
    g.new()
    g.run()
    g.show_go_screen()
