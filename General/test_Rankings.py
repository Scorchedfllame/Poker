from unittest import TestCase
from General.Rankings import *


class TestCheckFlush(TestCase):
    def test_pass(self):
        self.assertEqual(check_flush([(3, 2), (2, 2), (6, 2)]), 5060)

    def test_highest_pass(self):
        self.assertEqual(check_flush([(5, 2), (1, 2), (13, 2)]), 5140)

    def test_lowest_pass(self):
        self.assertEqual(check_flush([(2, 2), (3, 2), (4, 2)]), 5040)

    def test_fail_1(self):
        self.assertFalse(check_flush([(1, 2), (2, 2), (3, 0)]))

    def test_fail_2(self):
        self.assertFalse(check_flush([(3, 3), (3, 3), (3, 2)]))

    def test_fail_3(self):
        self.assertFalse(check_flush([(2, 3), (2, 2), (2, 1)]))

    def test_fail_4(self):
        self.assertFalse(check_flush([(1, 0), (2, 2), (3, 0)]))


class TestCheckFive(TestCase):
    def test_flush_pass(self):
        largest_score = check_five([(3, 1), (4, 1), (5, 1), (13, 1)], 3, check_flush)
        self.assertEqual(largest_score, 5130)

    def test_flush_fail(self):
        self.assertFalse(check_five([(3, 2), (4, 3), (5, 0), (13, 1)], 3, check_flush))

    def test_straight_pass(self):
        largest_score = check_five([(5, 1), (6, 3), (7, 2)], 3, check_straight)
        self.assertEqual(largest_score, 4070)

    def test_straight_fail(self):
        largest_score = check_five([(1, 2), (3, 0), (4, 0), (6, 0), (6, 2)], 3, check_straight)
        self.assertFalse(largest_score)

    def test_straight_flush_pass(self):
        largest_score = check_five([(9, 2), (8, 2), (11, 2), (12, 2), (13, 2)], 3, check_straight_flush)
        self.assertEqual(largest_score, 8130)

    def test_straight_flush_fail(self):
        largest_score = check_five([(9, 2), (7, 2), (10, 2), (12, 2), (13, 2)], 3, check_straight_flush)
        self.assertFalse(largest_score)


class TestCheckStraight(TestCase):
    def test_pass(self):
        largest_score = check_straight([(2, 1), (3, 2), (5, 1), (4, 0), (6, 0)])
        self.assertEqual(largest_score, 4060)

    def test_highest_pass(self):
        largest_score = check_straight([(12, 1), (10, 2), (9, 1), (11, 0), (13, 0), (1, 0)])
        self.assertEqual(largest_score, 4140)

    def test_lowest_pass(self):
        largest_score = check_straight([(1, 1), (3, 2), (5, 1), (4, 0), (2, 0)])
        self.assertEqual(largest_score, 4050)

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
        self.assertEqual(largest_score, 8060)

    def test_highest_pass(self):
        largest_score = check_straight_flush([(12, 3), (1, 3), (10, 3), (11, 3), (13, 3)])
        self.assertEqual(largest_score, 8140)

    def test_lowest_pass(self):
        largest_score = check_straight_flush([(1, 0), (3, 0), (5, 0), (4, 0), (2, 0)])
        self.assertEqual(largest_score, 8050)

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
        self.assertEqual(check_4_of_a_kind([(3, 0), (3, 2), (3, 1), (3, 3)]), 7030)


class TestCheckFullHouse(TestCase):
    def test_basic_pass(self):
        largest_score = check_full_house([(7, 1), (7, 2), (7, 3), (5, 2), (5, 0)])
        self.assertEqual(largest_score, 6190)

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
