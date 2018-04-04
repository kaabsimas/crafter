# -*- coding: latin-1
import os
from sys import path
path.append(os.path.join(os.getcwd(), 'tests'))

class Config:
    """ Disponibiliza informações comuns ao jogo definidas no arquivo settings.py """
    def __init__(self, params):
        if isinstance(params, basestring):
            self.__load_from_file(params)
        else:
            self.__load_from_dic(params)

    def __load_from_file(self, filename):
        # os.path
        settings = __import__(filename, globals(), locals(), [], -1)
        setting_vars = set(dir(settings)) - set(dir(__builtins__))
        for name in setting_vars:
            if name != '__file__' and name != '__builtins__':
                setattr(self, name.lower(), getattr(settings, name))

    def __load_from_dic(self, dic):
        for name, value in dic.iteritems():
            setattr(self, name.lower(), value)


if( __name__ == '__main__'):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    print dir_path
    print os.getcwd()
    conf = Config({})
    print conf.tileheight
