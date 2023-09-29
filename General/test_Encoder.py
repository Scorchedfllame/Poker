import unittest
from Encoder import *


class MyTestCase(unittest.TestCase):
    def Encoder(self):
        self.assertEqual(encode(['8 of Diamonds', '9 of Clubs', '10 of Spades']), [(8, 2), (9, 1), (10, 0)])


if __name__ == '__main__':
    unittest.main()
