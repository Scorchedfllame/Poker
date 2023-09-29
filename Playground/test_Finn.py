from unittest import TestCase
from Finn import *


class Test(TestCase):
    def test_player(self):
        amount_betting, amount_of_money_left, all_in = make_bet(100, 500)
        self.assertEqual(amount_betting, 100)
        self.assertEqual(amount_of_money_left, 400)
        self.assertEqual(all_in, False)

    def test_player1(self):
        amount_betting, amount_of_money_left, all_in = make_bet(1000, 500)
        self.assertEqual(amount_betting, 500)
        self.assertEqual(amount_of_money_left, 0)
        self.assertEqual(all_in, True)
