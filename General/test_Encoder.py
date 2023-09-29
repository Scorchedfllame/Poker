from unittest import *
from Encoder import *


class TestCardEncoder(TestCase):
    def test_encode_cards(self):
        self.assertEqual(encode_cards(['8 of Diamonds', '9 of Clubs', '10 of Spades']), [(8, 2), (9, 1), (10, 0)])

    def test_decode_cards(self):
        self.assertEqual(decode_cards([(8, 2), (9, 1), (10, 0)]), ['8 of Diamonds', '9 of Clubs', '10 of Spades'])
