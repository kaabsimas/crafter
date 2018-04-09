# -*- coding: latin-1 -*-
from crafter.config import Config
from unittest import TestCase
from pygame import Surface

class ConfigTestCase(TestCase):

    def tearDown(self):
        self.config = None

    def test_00_has_all_values(self):
        """ Verifica se o objeto possui todos os atributos passados ao instanciar """
        params = set(dir(self.config))
        expected = set(['size', 'tileheight', 'tilewidth', 'title'])

        self.assertEqual( params & expected, expected, "Alguma variável não foi importada")

    def test_01_get_map(self):
        """ Testa se os valores podem ser acessados atravez de notação de dicionário """
        self.assertEqual( self.config['size'], (200,200), "Valor retornado não é o esperado")

    def test_02_set_map(self):
        """ Testa se os valores podem ser alterados atravez de notação de dicionário """
        self.config['size'] = (300, 300)
        self.assertEqual( self.config['size'], (300,300), "Valor não alterado")

    def test_04_test_keys_method(self):
        """ Testa o método keys() """
        keys = self.config.keys()
        expected = ['size', 'title', 'tileheight', 'tilewidth']
        self.assertItemsEqual( keys, expected, "Método keys não retorna as chaves corretamente. O esperado era {0}, mas o recebido foi {1}".format(expected, keys))

class ConfigDicTestCase(ConfigTestCase):
    def setUp(self):
        """ Testa o objeto Config incializado com um dictionary do python """
        param = {'size': (200,200), 'title':"Objeto", 'tileHeight':40, 'tileWidth':60}
        self.config = Config(param)

    def test_03_title_name(self):
        """ Testa se os atributos foram carregados diferentemente de um objeto ou arquivo """
        self.assertEqual( self.config['title'], 'Objeto', 'Valor de título não condiz com o método utilizado')

class ConfigFileTestCase(ConfigTestCase):
    def setUp(self):
        """ Testa o objeto Config inicializado com um arquivo de configuração """
        self.config = Config('settings')

    def test_03_title_name(self):
        """ Testa se os atributos foram carregados diferentemente de um objeto ou arquivo """
        self.assertEqual( self.config['title'], 'Arquivo', 'Valor de título não condiz com o método utilizado')
