from unittest import TestCase
from General.Rankings import *


class TestCheckFlush(TestCase):
    def test_pass(self):
        self.assertEqual(check_flush([(1, 2), (2, 2), (3, 2)]), 3 * 10 ** 12)

    def test_fail(self):
        self.assertEqual(check_flush([(1, 2), (2, 2), (3, 0)]), False)


class TestCheckFive(TestCase):
    def test_flush_pass(self):
        largest_score = check_five([(3, 1), (4, 1), (5, 1), (13, 1)], 3, check_flush)
        self.assertEqual(largest_score, 13 * 10 ** 12)

    def test_flush_fail(self):
        self.assertFalse(check_five([(3, 2), (4, 3), (5, 0), (13, 1)], 3, check_flush))

    def test_straight_pass(self):
        largest_score = check_five([(5, 1), (6, 3), (7, 2)], 3, check_straight)
        self.assertEqual(largest_score, 7 * 10 ** 10)

    def test_straight_fail(self):
        largest_score = check_five([(1, 2), (3, 0), (4, 0), (6, 0), (6, 2)], 3, check_straight)
        self.assertFalse(largest_score)


class TestCheckStraight(TestCase):
    def test_pass(self):
        largest_score = check_straight([(2, 1), (3, 2), (5, 1), (4, 0), (6, 0)])
        self.assertEqual(largest_score, 6 * 10 ** 10)

    def test_fail(self):
        largest_score = check_straight([(1, 0), (2, 1), (3, 2), (6, 1), (4, 0)])
        self.assertFalse(largest_score)


class TestCheckStraightFlush(TestCase):
    def test_pass(self):
        largest_score = check_straight_flush([(2, 0), (3, 0), (5, 0), (4, 0), (6, 0)])
        self.assertEqual(largest_score, 6 * 10 ** 18)

    def test_fail(self):
        largest_score = check_straight_flush([(2, 1), (3, 2), (5, 1), (4, 0), (6, 0)])
        self.assertFalse(largest_score)

