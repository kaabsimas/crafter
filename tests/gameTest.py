# -*- coding: latin-1 -*-
from crafter.game import Game
from unittest import TestCase
from pygame import Surface

class GameTestCase(TestCase):
    def setUp(self):
        self.game = Game((200, 200))

    def tearDown(self):
        self.game = None

    def test_display(self):
        self.assertEqual(isinstance(self.game.screen, Surface), True) 

    def test_default_size(self):
        self.assertEqual(self.game.screen.get_size(), (200, 200), "Dimensões iniciais incorretas\n")
