# -*- coding: latin-1
import settings as settings

class Config:
    """ Disponibiliza informações comuns ao jogo definidas no arquivo settings.py """
    def __init__(self):
        setting_vars = set(dir(settings)) - set(dir(__builtins__))
        for name in setting_vars:
            if name != '__file__' and name != '__builtins__':
                setattr(self, name.lower(), getattr(settings, name))


if( __name__ == '__main__'):
    conf = Config()
    print conf.tileheight
