# -*- coding: latin-1 -*-
import pygame as pg
import os
import sys
from config import Config

class Game:
    def __init__(self, size, mode = 0):
        self.config = Config()
        pg.init()
        self.screen = pg.display.set_mode(size, mode)
        pg.display.set_caption(self.config.title)
        self.clock = pg.time.Clock()
        pg.key.set_repeat(500, 100)
        # self.load_data()

    def run(self):
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(self.config.fps) / 1000
            self.events()
            self.update()
            self.draw()

    def quit(self):
        pg.quit()
        sys.exit()

    def events(self):
        # catch all events here
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()

    def draw(self):
        self.screen.fill(self.config.bgcolor)
        pg.display.flip()

    def update(self):
        pass

    def set_bgcolor(self, color):
        self.bgcolor = color
