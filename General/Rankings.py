from Initialize.Game_Innit import *
from Encoder import *
from random import randint
import itertools


def rank_hand(hand):
    pass


deck = create_deck()
handTest = [deck[randint(1,13)] for i in range(7)]
print(decode_cards(handTest))
print(handTest)

# --Score Card--
# None: Royal Flush -> Highest Straight Flush--
# 13: Straight Flush--
# 13: Four of a Kind
# 13: Full House
# 13: Flush--
# 13: Straight--
# 13: Three of a kind
# 13: Two Pair
# 13: Pair
# 13: High Card
# 13: Kicker


def check_flush(cards: list):
    if all(i[1] == cards[0][1] for i in cards):
        return score_for_highest(cards, 12)
    return False


def score_for_highest(cards:list, multiplier):
    return max([x[0] for x in cards]) * 10 ** multiplier


def check_straight_flush(cards: list):
    if check_flush(cards) and check_straight(cards):
        return score_for_highest(cards, 18)
    return False


def check_straight(cards:list):
    sort = sorted([i[0] for i in cards])
    for x in range(len(sort)):
        if not(sort[x] - sort[x-1] == 1) and x > 0:
            return False
    return score_for_highest(cards, 10)


def check_n_of_a_kind(n: int, cards: list):
    highest = 0
    for i in list(itertools.combinations(cards, n)):
        if all(i[0][0] == x[0] for x in i):
            highest = max(i[0][0], highest)
    return highest


def check_five(cards: list, size: int, checker):
    val = []
    for i in list(itertools.combinations(cards, size)):
        val.append(checker(i))
    return max(val)





