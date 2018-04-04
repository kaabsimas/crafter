# -*- coding: latin-1 -*-

class ScenarioList:
    """ Cria, armazena e carrega cenários de jogo """
    active = None
    list = {}

    def __init__(self, game):
        self.game = game

    def add(self, name, className):
        self.list[name] = className

    def load(self, name, *args, **kwargs):
        if( name in self.list ):
            self.active = self.list[name](self.game, *args, **kwargs
            if( hasattr(self.active, 'new') ):
                self.active.new()
