# -*- coding: latin-1 -*-

class ScenarioList:
    """ Cria, armazena e carrega cenários de jogo """
    active = None
    list = {}

    def __init__(self, game):
        self.game = game

    def add(self, name, className):
        self.list[name] = className

    def load(self, name, params=None):
        if( name in self.list) ):
            if( params != None )
                self.active = self[name](self.game, params)
            else
                self.active = self[name](self.game)
            if( hasattr(self.active, 'new') ):
                self.active.new()
