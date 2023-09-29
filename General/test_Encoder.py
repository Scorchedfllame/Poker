import unittest
from Encoder import *


class MyTestCase(unittest.TestCase):
    def test_encoder(self):
        self.assertEqual(encode(['8 of Diamonds', '9 of Clubs', '10 of Spades']), [(8, 2), (9, 1), (10, 0)])

    def test_decoder(self):
        self.assertEqual(decode([(8, 2), (9, 1), (10, 0)]), ['8 of Diamonds', '9 of Clubs', '10 of Spades'])


if __name__ == '__main__':
    unittest.main()
