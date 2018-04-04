# -*- coding: latin-1 -*-
from crafter.config import Config
from unittest import TestCase
from pygame import Surface

class ConfigTestCase(TestCase):

    def tearDown(self):
        self.config = None

    def test_has_all_values(self):
        """ Verifica se o objeto possui todos os atributos passados ao instanciar """
        params = set(dir(self.config))
        expected = set(['size', 'tileheight', 'tilewidth', 'title'])

        self.assertEqual( params & expected, expected, "Alguma variável não foi importada")

class ConfigDicTestCase(ConfigTestCase):
    def setUp(self):
        """ Testa o objeto Config incializado com um dictionary do python """
        param = {'size': (200,200), 'title':"Objeto", 'tileHeight':40, 'tileWidth':60}
        self.config = Config(param)

class ConfigFileTestCase(ConfigTestCase):
    def setUp(self):
        """ Testa o objeto Config inicializado com um arquivo de configuração """
        self.config = Config('settings')
