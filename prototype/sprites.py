import pygame as pg
from pygame.locals import *
from settings import *

class Player(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILEWIDTH / 2, TILEWIDTH / 2))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y

    def move(self, dx=0, dy=0):
        self.x += dx
        self.y += dy

    def update(self):
        origin = (((self.x-self.y)*TILEWIDTH/2) + WIDTH/2 - self.rect.width/2, ((self.x+self.y)*TILEHEIGHT/2) + 40 )
        self.rect.x = origin[0]#self.x * TILEWIDTH
        self.rect.y = origin[1]#self.y * TILEHEIGHT
        font = pg.font.Font(None, 12)
        text = font.render("(%s, %s)"%(self.x,self.y), 1, BLUE)
        textpos = text.get_rect(centerx = self.image.get_width()/2, centery = -10 + self.image.get_height()/2)
        self.image.fill(YELLOW)
        self.image.blit(text, textpos)

class Tile(pg.sprite.Sprite):
    def __init__(self, game, index, x, y):
        self.groups = game.tiles
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILEWIDTH, TILEHEIGHT + 10), SRCALPHA)
        # origin = (((x-y)*TILEWIDTH/2) + WIDTH/2, ((x+y)*TILEHEIGHT/2) + 50 + ( 5 if index < 4 else 0))
        # area = ( index * TILEWIDTH, 0, TILEWIDTH, tilesRect[3] )
        # dest = ( origin[0] + (-TILEWIDTH / 2), origin[1], origin[0]+TILEWIDTH, origin[1]+tilesRect[3] )
        # self.screen.blit(tiles, dest, area)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = ((self.x-self.y)*TILEWIDTH/2) + self.game.map.rect.width/2 + (-TILEWIDTH / 2)
        self.rect.y = ((self.x+self.y)*TILEHEIGHT/2) + ( 5 if index < 4 else 0)
        area = ( (index * TILEWIDTH)+1, 0, TILEWIDTH, self.game.tilesRect[3])
        self.image.blit(self.game.tilesSrc, (0, -10, TILEWIDTH, TILEHEIGHT), area)
        font = pg.font.Font(None, 12)
        text = font.render("(%s, %s)"%(x,y), 1, BLACK)
        textpos = text.get_rect(centerx = self.image.get_width()/2, centery = -10 + self.image.get_height()/2)
        self.image.blit(text, textpos)
        # pg.draw.polygon(self.image, GREEN, ((0, 0), (TILEWIDTH -1, 0), (TILEWIDTH -1, TILEHEIGHT -1), (0, TILEHEIGHT)), 1)
