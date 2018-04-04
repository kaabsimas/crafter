# -*- coding: latin-1 -*-
from crafter import *
from unittest import TestCase

class ScenarioListTestCase(TestCase):
    def setUp(self):
        g = game.Game((500, 600))
        self.list = scenarioList.ScenarioList(g)

    def tearDown(self):
        self.list = None

    def test_default_list(self):
        self.assertEqual(self.list.list, {}, "Lista inicial incorreta\n")

    def test_list_addition(self):
        self.list.add("first", "test")
        self.assertEqual(self.list.list, {'first':'test'}, "Valor inserido não armazenado\n")
