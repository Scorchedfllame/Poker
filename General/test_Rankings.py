from unittest import TestCase
from General.Rankings import *


class TestCheckFlush(TestCase):
    def test_check_flush(self):
        self.assertEqual(check_flush([(1, 2), (2, 2), (3, 2)]), 3 * 10 ** 12)


class TestCheckFive(TestCase):
    def test_flush(self):
        largest_score = check_five([(0, 1), (1,1), (2,1), (3,1), (4,1), (5,1), (13,1)], 5, check_flush)
        self.assertEqual(largest_score, 13 * 10 ** 12)


class TestCheckStraight(TestCase):
    def test_pass(self):
        largest_score = check_five([(1, 0), (2, 1), (3, 2), (5, 1), (4, 0), (6, 0), (7, 1)], 5, check_straight)
        self.assertEqual(largest_score, 7 * 10 ** 10)

    def test_fail(self):
        largest_score = check_five([(1, 0), (2, 1), (3, 2), (6, 1), (4, 0)], 5, check_straight)
        self.assertFalse(largest_score)


class TestCheckStraightFlush(TestCase):
    def test_pass(self):
        largest_score = check_five([(1, 0), (2, 0), (3, 0), (5, 0), (4, 0), (6, 0), (7, 1)], 5, check_straight_flush)
        self.assertEqual(largest_score, 6 * 10 ** 18)

    def test_fail(self):
        largest_score = check_five([(1, 0), (2, 1), (3, 2), (5, 1), (4, 0), (6, 0), (7, 1)], 5, check_straight_flush)
        self.assertFalse(largest_score)
