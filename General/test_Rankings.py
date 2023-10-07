from unittest import TestCase
from General.Rankings import *
from General.Encoder import *
from Initialize.Game_Innit import *


def create_new_deck():
    deck = create_deck()
    keys = decode_cards([(card.value, card.suit) for card in deck])
    cards = {}
    for i in range(len(keys)):
        cards[keys[i]] = deck[i]
    return cards


class TestCheckForAll(TestCase):
    def test_royal_flush(self):
        cards = create_new_deck()
        royal_flush = check_for_all(
            [
                cards['Ace of Spades'], cards["2 of Clubs"], cards["Queen of Spades"], cards["3 of Diamonds"],
                cards['King of Spades'], cards["Jack of Spades"], cards["10 of Spades"]
            ],
            5)
        self.assertEqual(9001400, royal_flush)

    def test_royal_flush_tie(self):
        cards = create_new_deck()
        royal_flush_1 = check_for_all(
            [
                cards['Ace of Diamonds'], cards["2 of Clubs"], cards["Queen of Diamonds"], cards["3 of Diamonds"],
                cards['King of Diamonds'], cards["Jack of Diamonds"], cards["10 of Diamonds"]
            ],
            5)
        royal_flush_2 = check_for_all(
            [
                cards['Ace of Spades'], cards["2 of Clubs"], cards["Queen of Spades"], cards["3 of Diamonds"],
                cards['King of Spades'], cards["Jack of Spades"], cards["10 of Spades"]
            ],
            5)
        self.assertEqual(royal_flush_2, royal_flush_1)

    def test_four_of_a_kind(self):
        cards = create_new_deck()
        four_of_a_kind = check_for_all(
            [
                cards['King of Spades'], cards["King of Clubs"], cards["10 of Spades"], cards["King of Diamonds"],
                cards['King of Hearts'], cards["Jack of Diamonds"], cards["Ace of Spades"]
            ],
            5
        )
        self.assertEqual(8001309.1, four_of_a_kind)

    def test_four_of_a_kind_kicker(self):
        cards = create_new_deck()
        four_of_a_kind_1 = check_for_all(
            [
                cards['King of Spades'], cards["King of Clubs"], cards["10 of Spades"], cards["King of Diamonds"],
                cards['King of Hearts'], cards["Jack of Diamonds"], cards["King of Spades"]
            ],
            5
        )
        four_of_a_kind_2 = check_for_all(
            [
                cards['King of Spades'], cards["King of Clubs"], cards["10 of Spades"], cards["King of Diamonds"],
                cards['King of Hearts'], cards["Jack of Diamonds"], cards["Ace of Spades"]
            ],
            5
        )
        self.assertGreater(four_of_a_kind_2, four_of_a_kind_1)

    def test_full_house(self):
        cards = create_new_deck()
        full_house = check_for_all(
            [
                cards['King of Spades'], cards["King of Clubs"], cards["10 of Spades"], cards["King of Diamonds"],
                cards['Jack of Hearts'], cards["Jack of Diamonds"], cards["Ace of Spades"]
            ],
            5
        )
        self.assertEqual(7131100, full_house)

    def test_full_house_secondary(self):
        cards = create_new_deck()
        full_house_1 = check_for_all(
            [
                cards['King of Spades'], cards["King of Clubs"], cards["10 of Spades"], cards["King of Diamonds"],
                cards['Jack of Hearts'], cards["Jack of Diamonds"], cards["Ace of Spades"]
            ],
            5
        )
        full_house_2 = check_for_all(
            [
                cards['King of Spades'], cards["King of Clubs"], cards["10 of Spades"], cards["King of Diamonds"],
                cards['Queen of Hearts'], cards["Queen of Diamonds"], cards["Ace of Spades"]
            ],
            5
        )
        self.assertGreater(full_house_2, full_house_1)

    def test_flush(self):
        cards = create_new_deck()
        flush = check_for_all(
            [
                cards['King of Spades'], cards["4 of Spades"], cards["10 of Spades"], cards["King of Diamonds"],
                cards['Ace of Hearts'], cards["Jack of Spades"], cards["Ace of Spades"]
            ],
            5
        )
        self.assertEqual(6002327, flush)

    def test_flush_quinary(self):
        cards = create_new_deck()
        flush_1 = check_for_all(
            [
                cards['King of Spades'], cards["4 of Spades"], cards["10 of Spades"], cards["King of Diamonds"],
                cards['Ace of Hearts'], cards["Jack of Spades"], cards["Ace of Spades"]
            ],
            5
        )
        flush_2 = check_for_all(
            [
                cards['King of Spades'], cards["5 of Spades"], cards["10 of Spades"], cards["King of Diamonds"],
                cards['Ace of Hearts'], cards["Jack of Spades"], cards["Ace of Spades"]
            ],
            5
        )
        self.assertGreater(flush_2, flush_1)

    def test_straight(self):
        cards = create_new_deck()
        straight = check_for_all(
            [
                cards['5 of Spades'], cards["4 of Clubs"], cards["6 of Spades"], cards["7 of Diamonds"],
                cards['Ace of Hearts'], cards["8 of Spades"], cards["9 of Diamonds"]
            ],
            5
        )
        self.assertEqual(5000900, straight)

    def test_straight_tie(self):
        cards = create_new_deck()
        straight_1 = check_for_all(
            [
                cards['5 of Spades'], cards["4 of Clubs"], cards["6 of Spades"], cards["7 of Diamonds"],
                cards['Ace of Hearts'], cards["8 of Spades"], cards["9 of Diamonds"]
            ],
            5
        )
        straight_2 = check_for_all(
            [
                cards['5 of Clubs'], cards["4 of Spades"], cards["6 of Clubs"], cards["7 of Hearts"],
                cards['2 of Hearts'], cards["8 of Clubs"], cards["9 of Hearts"]
            ],
            5
        )
        self.assertEqual(straight_2, straight_1)

    def test_three_of_a_kind(self):
        cards = create_new_deck()
        straight = check_for_all(
            [
                cards['5 of Spades'], cards["5 of Clubs"], cards["King of Spades"], cards["7 of Diamonds"],
                cards['Ace of Hearts'], cards["8 of Spades"], cards["5 of Diamonds"]
            ],
            5
        )
        self.assertEqual(4000515.86, straight)

    def test_two_pair(self):
        cards = create_new_deck()
        two_pair = check_for_all(
            [
                cards['5 of Spades'], cards["5 of Clubs"], cards["King of Spades"], cards["7 of Diamonds"],
                cards['Ace of Hearts'], cards["8 of Spades"], cards["8 of Diamonds"]
            ],
            5
        )
        self.assertEqual(3080509.1, two_pair)

    def test_pair(self):
        cards = create_new_deck()
        straight = check_for_all(
            [
                cards['5 of Spades'], cards["3 of Clubs"], cards["King of Spades"], cards["7 of Diamonds"],
                cards['Ace of Hearts'], cards["6 of Spades"], cards["5 of Diamonds"]
            ],
            5
        )
        self.assertEqual(2000518.59, straight)

    def test_high_card(self):
        cards = create_new_deck()
        straight = check_for_all(
            [
                cards['5 of Spades'], cards["Queen of Clubs"], cards["King of Spades"], cards["7 of Diamonds"],
                cards['Ace of Hearts'], cards["8 of Spades"], cards["10 of Diamonds"]
            ],
            5
        )
        self.assertEqual(1002418, straight)


class TestSetInHand(TestCase):
    def test_true(self):
        deck = create_new_deck()
        cards = list(deck.values())
        set_in_hand(cards)
        for card in cards:
            self.assertTrue(card.in_hand)

    def test_false(self):
        deck = create_new_deck()
        cards = list(deck.values())
        set_in_hand(cards, in_hand=False)
        for card in cards:
            self.assertFalse(card.in_hand)


class TestGetHighestCard(TestCase):
    def test_ace(self):
        cards = create_new_deck()
        ace = get_highest_card([
            cards['Ace of Spades'], cards['King of Hearts'], cards["2 of Diamonds"], cards['5 of Clubs']
        ])
        self.assertEqual(cards['Ace of Spades'], ace)
