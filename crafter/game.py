# -*- coding: latin-1 -*-
import pygame as pg
import os
import sys
from scenarioList import ScenarioList
from config import Config

class Game:
    def __init__(self, size, mode = 0):
        self.config = Config()
        self.screen = pg.display.set_mode(size, mode)
        pg.display.set_caption(self.config.title)
        self.clock = pg.time.Clock()
        pg.key.set_repeat(500, 100)
        self.eventQueue = None
        self.scenario = ScenarioList(self)

    def run(self):
        pg.init()
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(self.config.fps) / 1000
            self.events()
            self.update()
            self.draw()

    def events(self):
        # catch all events here
        self.eventQueue = pg.event.get()
        self.__call(self.scenario.active, 'events')
        for event in self.eventQueue:
            if event.type == pg.QUIT:
                self.quit()
        self.eventQueue = None

    def update(self):
        self.__call( self.scenario.active, 'update')

    def draw(self):
        self.__call( self.scenario.active, 'draw')
        pg.display.flip()

    def quit(self):
        pg.quit()
        sys.exit()

    def __call(self, obj, method, params=None):
        if( hasattr(obj, method) ):
            func = getattr( obj, method )
            if( callable(func) ):
                if( params != None ):
                    func(params)
                else:
                    func()

if( __name__ == '__main__' ):
    g = Game((200,200))
    g.run()
