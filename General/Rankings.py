import itertools
from General.Classes import Card


def rank_hand(hand):
    pass


# --Score Card--
# (((
#    9: Royal Flush -> Highest Straight Flush
#    9: Straight Flush
#    8: Four of a Kind
#    7: Full House
#    6: Flush
#    5: Straight
#    4: Three of a kind
#    3: Two Pair
#    2: Pair
#    1: High Card
# ))) First digit
#
# Middle 4 digits denote the inbetween
#
# Last 2 Digits: Kicker


def get_card_values(cards: list[Card]):
    return [(card.value, card.suit) for card in cards]


def set_in_hand(cards: list[Card], in_hand=True):
    for card in cards:
        card.in_hand = in_hand


def check_flush(cards: list[Card]):
    if all(i.suit == cards[0].suit for i in cards):
        return (check_high_card(cards) - 1000000) + 6000000
    return False


def score_for_highest(cards: list[Card]):
    return sorted(cards, reverse=True, key=lambda x: x.value)[0]


def check_straight_flush(cards: list[Card]):
    straight = check_straight(cards)
    if check_flush(cards) and straight:
        return straight + 4000000
    return False


def check_straight(cards: list[Card]):
    nums = [card.value for card in cards]
    if 2 in nums:
        for i in range(len(nums)):
            if nums[i] == 14:
                nums[i] = 1
    sort = sorted(nums)
    for x in range(len(sort)):
        if not(sort[x] - sort[x-1] == 1) and x > 0:
            return False
    set_in_hand(cards)
    if 2 in nums:
        for i in range(len(nums)):
            if nums[i] == 1:
                cards[i].value = 14
        return 5000000 + 500
    return score_for_highest(cards).value * 100 + 5000000


def check_n_of_a_kind(n: int, cards: list[Card], amount=1):
    highest = []
    for i in list(itertools.combinations(cards, n)):
        if all(i[0].value == x.value for x in i):
            highest.append(i)
    if highest:
        if amount != 1:
            return sorted(highest, reverse=True, key=lambda x: x[0].value)[:amount]
        return sorted(highest, reverse=True, key=lambda x: x[0].value)[0]
    return False


def check_4_of_a_kind(cards: list[Card]):
    matches = check_n_of_a_kind(4, cards)
    if matches:
        set_in_hand(matches)
        return matches[0].value * 100 + 8000000
    return False


def check_3_of_a_kind(cards: list[Card]):
    matches = check_n_of_a_kind(3, cards)
    if matches:
        set_in_hand(matches)
        return matches[0].value * 100 + 4000000
    return False


def check_pair(cards: list[Card]):
    matches = check_n_of_a_kind(2, cards)
    if matches:
        set_in_hand(matches)
        return matches[0].value * 100 + 2000000
    return False


def check_2_pair(cards: list[Card]):
    firsts = check_n_of_a_kind(2, cards, amount=2)
    if firsts:
        if len(firsts) == 2 and firsts[0] and firsts[1]:
            set_in_hand(firsts[0] + firsts[1])
            return firsts[0][0].value * 10000 + firsts[1][1].value * 100 + 3000000
    return False


def check_full_house(cards: list[Card]):
    confirm_three = False
    confirm_two = False
    total = 0
    three = check_n_of_a_kind(3, cards)
    if three:
        set_in_hand(three)
        total += three[0].value * 10000
        confirm_three =True
    second = check_n_of_a_kind(2, cards, amount=4)
    if second:
        for i in second:
            if [card for card in i if card.in_hand is False]:
                set_in_hand(i)
                total += i[0].value * 100
                confirm_two = True
    if confirm_three and confirm_two:
        return total + 7000000
    return False


def check_high_card(cards: list[Card]):
    total = 0
    multiplier = 5
    while [card for card in cards if card.in_hand is False]:
        high = score_for_highest([card for card in cards if card.in_hand is False])
        high.in_hand = True
        total += high.value * (multiplier * 13)
        multiplier -= 1
    return total + 1000000


def add_kicker(cards: list[Card]):
    if cards:
        return (check_high_card(cards) - 1000000) / 100
    return False


def check_five(cards: list, size: int, checker):
    val = []
    for i in list(itertools.combinations(cards, size)):
        score = checker(i)
        kicker = add_kicker([card for card in i if card.in_hand is False])
        if kicker:
            score += kicker
        val.append(score)
        set_in_hand(cards, in_hand=False)
    return max(val)


def check_for_all(cards: list, size: int):
    maximum = []
    functions = [check_straight_flush, check_4_of_a_kind, check_full_house, check_flush, check_straight,
                 check_3_of_a_kind, check_2_pair, check_pair, check_high_card]
    for i in functions:
        curr = check_five(cards, size, i)
        if curr:
            maximum.append(curr)
    return sorted(maximum, reverse=True)[0]
