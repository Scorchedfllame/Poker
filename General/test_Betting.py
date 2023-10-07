from unittest import TestCase
from General.Betting import *


class TestMakeBet(TestCase):
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


class TestFold(TestCase):
    def test_fold(self):
        player_1 = Player('John')
        fold(1000, player_1)
        self.assertTrue(player_1.folded)


class TestCheck(TestCase):
    def test_big_blind_check(self):
        player_1 = Player('Jake')
        player_1.curr_bet = 15
        player_1.money = 2000
        check = can_check(15, player_1)
        self.assertTrue(check)

    def test_big_blind_cant_check(self):
        player_1 = Player('Jill')
        player_1.curr_bet = 15
        player_1.money = 2000
        check = can_check(125, player_1)
        self.assertFalse(check)

    def test_first(self):
        player_1 = Player('Josh')
        player_1.money = 100
        check = can_check(0, player_1)
        self.assertTrue(check)
        self.assertEqual(100, player_1.money)
        self.assertFalse(player_1.all_in, player_1.folded)

    def test_all_in(self):
        player_1 = Player("Jack")
        player_1.all_in = True
        player_1.money = 0
        check = can_check(1000000, player_1)
        self.assertTrue(check)
        self.assertTrue(player_1.all_in, not player_1.folded)
        self.assertEqual(player_1.money, 0)

    def test_cant_check(self):
        player_1 = Player("James")
        player_1.money = 30
        player_1.curr_bet = 5
        check = can_check(10, player_1)
        self.assertFalse(check)


class TestRaiseBet(TestCase):
    def test_first_raise(self):
        player_1 = Player('Jammie')
        player_1.curr_bet = 0
        player_1.money = 1500
        raise_bet(0, player_1, 15)
        self.assertEqual(15, player_1.curr_bet)
        self.assertFalse(player_1.all_in, player_1.folded)

    def test_basic_raise(self):
        player_1 = Player('Joe')
        player_1.curr_bet = 0
        player_1.money = 1500
        raise_bet(15, player_1, 15)
        self.assertEqual(1500 - 30, player_1.money)
        self.assertEqual(30, player_1.curr_bet)
        self.assertFalse(player_1.all_in, player_1.folded)

    def test_all_in(self):
        player_1 = Player('Jocelyn')
        player_1.curr_bet = 25
        player_1.money = 150
        raise_bet(120, player_1, 100000)
        self.assertEqual(0, player_1.money)
        self.assertEqual(175, player_1.curr_bet)
        self.assertTrue(player_1.all_in)
        self.assertFalse(player_1.folded)


class TestCall(TestCase):
    def test_check(self):
        player_1 = Player('Jim')
        player_1.money = 1000
        player_1.curr_bet = 0
        call(0, player_1)
        self.assertEqual(0, player_1.curr_bet)
        self.assertFalse(player_1.all_in, player_1.folded)

    def test_basic(self):
        player_1 = Player('Jaquifa')
        player_1.money = 1500
        player_1.curr_bet = 0
        call(15, player_1)
        self.assertEqual(15, player_1.curr_bet)
        self.assertFalse(player_1.all_in, player_1.folded)

    def test_all_in(self):
        player_1 = Player('Jaclyn')
        player_1.money = 125
        player_1.curr_bet = 0
        call(500, player_1)
        self.assertEqual(125, player_1.curr_bet)
        self.assertTrue(player_1.all_in)
        self.assertFalse(player_1.folded)
