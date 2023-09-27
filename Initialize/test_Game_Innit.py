from unittest import TestCase
from Initialize.Game_Innit import *


class TestCreateDeck(TestCase):
    def test_first_card(self):
        test_deck = create_deck()
        self.assertEqual("Ace of Spades", test_deck[0])

    def test_last_card(self):
        test_deck = create_deck()
        self.assertEqual("King of Hearts", test_deck[-1])
