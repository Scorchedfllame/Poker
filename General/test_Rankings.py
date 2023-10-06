from unittest import TestCase
from General.Rankings import *
from Initialize.Game_Innit import create_deck
from General.Encoder import *

def create_new_deck():
    deck = create_deck()
    keys = decode_cards([(card.value, card.suit) for card in deck])
    cards = {}
    for i in range(len(keys)):
        cards[keys[i]] = deck[i]
    return cards


class TestCheckFlush(TestCase):
    def test_pass(self):
        self.assertEqual(check_flush([(3, 2), (2, 2), (6, 2)]), 6060)

    def test_highest_pass(self):
        self.assertEqual(check_flush([(5, 2), (1, 2), (13, 2)]), 6140)

    def test_lowest_pass(self):
        self.assertEqual(check_flush([(2, 2), (3, 2), (4, 2)]), 6040)

    def test_fail_1(self):
        self.assertFalse(check_flush([(1, 2), (2, 2), (3, 0)]))

    def test_fail_2(self):
        self.assertFalse(check_flush([(3, 3), (3, 3), (3, 2)]))

    def test_fail_3(self):
        self.assertFalse(check_flush([(2, 3), (2, 2), (2, 1)]))

    def test_fail_4(self):
        self.assertFalse(check_flush([(1, 0), (2, 2), (3, 0)]))


class TestCheckStraight(TestCase):
    def test_pass(self):
        largest_score = check_straight([(2, 1), (3, 2), (5, 1), (4, 0), (6, 0)])
        self.assertEqual(largest_score, 5060)

    def test_highest_pass(self):
        largest_score = check_straight([(12, 1), (10, 2), (9, 1), (11, 0), (13, 0), (1, 0)])
        self.assertEqual(largest_score, 5140)

    def test_lowest_pass(self):
        largest_score = check_straight([(1, 1), (3, 2), (5, 1), (4, 0), (2, 0)])
        self.assertEqual(largest_score, 5050)

    def test_fail_1(self):
        largest_score = check_straight([(1, 0), (2, 1), (3, 2), (6, 1), (4, 0)])
        self.assertFalse(largest_score)

    def test_fail_2(self):
        largest_score = check_straight([(1, 0), (1, 1), (2, 2), (3, 1), (4, 0)])
        self.assertFalse(largest_score)

    def test_fail_3(self):
        largest_score = check_straight([(2, 0), (2, 1), (2, 2), (2, 1), (2, 0)])
        self.assertFalse(largest_score)

    def test_fail_4(self):
        largest_score = check_straight([(13, 0), (12, 1), (11, 2), (10, 1), (2, 0)])
        self.assertFalse(largest_score)


class TestCheckStraightFlush(TestCase):
    def test_pass(self):
        largest_score = check_straight_flush([(2, 0), (3, 0), (5, 0), (4, 0), (6, 0)])
        self.assertEqual(largest_score, 9060)

    def test_highest_pass(self):
        largest_score = check_straight_flush([(12, 3), (1, 3), (10, 3), (11, 3), (13, 3)])
        self.assertEqual(largest_score, 9140)

    def test_lowest_pass(self):
        largest_score = check_straight_flush([(1, 0), (3, 0), (5, 0), (4, 0), (2, 0)])
        self.assertEqual(largest_score, 9050)

    def test_fail_1(self):
        largest_score = check_straight_flush([(2, 1), (3, 2), (5, 1), (4, 0), (6, 0)])
        self.assertFalse(largest_score)

    def test_fail_2(self):
        largest_score = check_straight_flush([(3, 0), (3, 0), (5, 0), (4, 0), (6, 0)])
        self.assertFalse(largest_score)

    def test_fail_3(self):
        largest_score = check_straight_flush([(2, 1), (3, 0), (5, 0), (4, 0), (6, 0)])
        self.assertFalse(largest_score)

    def test_fail_4(self):
        largest_score = check_straight_flush([(2, 1), (3, 1), (5, 1), (5, 1), (6, 1)])
        self.assertFalse(largest_score)


class TestCheckNCards(TestCase):
    def test_check_2_of_a_kind_pass(self):
        largest_score = check_n_of_a_kind(2, [(2, 2), (1, 3), (2, 1), (1, 0), (2, 0)])
        self.assertEqual(largest_score, 2)

    def test_check_3_of_a_kind_pass(self):
        largest_score = check_n_of_a_kind(3, [(3, 1), (3, 0), (3, 3), (2, 2), (2, 0)])
        self.assertEqual(largest_score, 3)

    def test_check_4_of_a_kind_pass(self):
        largest_score = check_n_of_a_kind(4, [(4, 3), (4, 1), (4, 2), (4, 0), (5, 2)])
        self.assertEqual(largest_score, 4)

    def test_check_2_of_a_kind_fail(self):
        largest_score = check_n_of_a_kind(2, [(2, 2), (1, 3), (3, 1), (4, 0), (13, 0)])
        self.assertFalse(largest_score)

    def test_check_3_of_a_kind_fail(self):
        largest_score = check_n_of_a_kind(3, [(2, 2), (2, 3), (3, 1), (4, 0), (13, 0)])
        self.assertFalse(largest_score)

    def test_check_4_of_a_kind_fail(self):
        largest_score = check_n_of_a_kind(4, [(2, 2), (2, 3), (2, 1), (4, 0), (13, 0)])
        self.assertFalse(largest_score)


class TestBasicPairs(TestCase):
    def test_check_4_of_a_kind(self):
        self.assertEqual(check_4_of_a_kind([(3, 0), (3, 2), (3, 1), (3, 3)]), 8030)


class TestCheckFullHouse(TestCase):
    def test_basic_pass(self):
        largest_score = check_full_house([(7, 1), (7, 2), (7, 3), (5, 2), (5, 0)])
        self.assertEqual(largest_score, 7190)

    def test_secondary(self):
        largest_score_1 = check_full_house([(5, 0), (5, 1), (5, 3), (2, 1), (2, 2)])
        largest_score_2 = check_full_house([(5, 0), (5, 1), (5, 2), (3, 2), (3, 1)])
        self.assertGreater(largest_score_2, largest_score_1)

    def test_basic_fail_1(self):
        self.assertFalse(check_full_house([(6, 0), (6, 1), (5, 0), (5, 1), (4, 0)]))

    def test_basic_fail_2(self):
        self.assertFalse(check_full_house([(5, 0), (6, 0), (7, 0), (8, 0), (9, 0)]))

    def test_basic_fail_3(self):
        self.assertFalse(check_full_house([(2, 0), (2, 1), (2, 0), (1, 1), (4, 0)]))


class TestCheckForAll(TestCase):
    def test_check_royal_flush(self):
        cards = create_new_deck()
        royal_flush = check_for_all(
            [cards['Ace of Spades'], cards['King of Spades'], cards['Queen of Spades'], cards['2 of Hearts']],
            3)
        self.assertEqual(royal_flush, 9140)
        self.assertTrue(royal_flush)

    def test_check_high_card(self):
        cards = create_new_deck()
        cards['6 of Diamonds'].pocket = True
        high_card = check_for_all(
            [cards['8 of Clubs'], cards['6 of Diamonds'], cards['5 of Spades']],
            3)
        self.assertEqual(1166, high_card)
        self.assertTrue(high_card)

    def test_check_kicker_1(self):
        cards = create_new_deck()
        cards['Jack of Hearts'].pocket = True
        cards['Jack of Diamonds'].pocket = True
        score_1 = check_for_all(
            [cards['Jack of Hearts'], cards['Ace of Diamonds']],
            2)
        score_2 = check_for_all(
            [cards['Jack of Diamonds'], cards['King of Spades']],
            2)
        self.assertGreater(score_1, score_2)
        self.assertTrue(score_1, score_2)

    def test_check_kicker_2(self):
        cards = create_new_deck()
        pass

