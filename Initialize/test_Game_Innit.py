from unittest import TestCase
from Initialize.Game_Innit import *


class TestCreateDeck(TestCase):
    def test_first_card(self):
        test_deck = create_deck()
        self.assertEqual(2, test_deck[0].value)
        self.assertEqual(0, test_deck[0].suit)

    def test_last_card(self):
        test_deck = create_deck()
        self.assertEqual(14, test_deck[-1].value)
        self.assertEqual(3, test_deck[-1].suit)
