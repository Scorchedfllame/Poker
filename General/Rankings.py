import itertools


def rank_hand(hand):
    pass


# --Score Card--
# 9: Royal Flush -> Highest Straight Flush--
# 9: Straight Flush--
# 8: Four of a Kind--
# 7: Full House--
# 6: Flush--
# 5: Straight--
# 4: Three of a kind--
# 3: Two Pair--
# 2: Pair--
# 1: High Card--
# First Digit: Kicker--


def check_flush(cards: list):
    if all(i[1] == cards[0][1] for i in cards):
        if 1 in [x[0] for x in cards]:
            return 6140
        return score_for_highest(cards) + 6000
    return False


def score_for_highest(cards: list, multiplier=10):
    return max([x[0] for x in cards]) * multiplier


def check_straight_flush(cards: list):
    straight = check_straight(cards)
    if check_flush(cards) and straight:
        return straight + 4000
    return False


def check_straight(cards: list):
    nums = [i[0] for i in cards]
    if 13 in nums:
        for i in range(len(nums)):
            if nums[i] == 1:
                nums[i] = 14
    sort = sorted(nums)
    for x in range(len(sort)):
        if not(sort[x] - sort[x-1] == 1) and x > 0:
            return False
    if 14 in nums:
        return 5140
    return score_for_highest(cards) + 5000


def check_n_of_a_kind(n: int, cards: list, amount=1):
    highest = [0]
    for i in list(itertools.combinations(cards, n)):
        if all(i[0][0] == x[0] for x in i):
            highest.append(i[0][0])
    if amount != 1:
        return sorted(highest, reverse=True)[:amount]
    return sorted(highest, reverse=True)[0]


def check_4_of_a_kind(cards: list):
    value = check_n_of_a_kind(4, cards)
    if value:
        return value * 10 + 8000
    return False


def check_3_of_a_kind(cards: list):
    value = check_n_of_a_kind(3, cards)
    if value:
        return value * 10 + 4000
    return False


def check_pair(cards: list):
    value = check_n_of_a_kind(3, cards)
    if value:
        return value * 10 + 2000
    return False


def check_2_pair(cards: list):
    firsts = [check_n_of_a_kind(2, cards)]
    if len(firsts) >= 2:
        if firsts[0] and firsts[1]:
            return firsts[0] * 20 + firsts[1] * 10 + 3000
    return False


def check_full_house(cards: list):
    two = 0
    three = check_n_of_a_kind(3, cards)
    second = check_n_of_a_kind(2, cards, amount=4)
    for i in second:
        if three != i:
            two = i
    if two and three:
        return (three * 20) + (two * 10) + 7000
    return False


def check_high_card(cards: list):
    if 1 in [x[0] for x in cards]:
        return 14 * 20 + 1000
    return score_for_highest(cards, 20) + 1000


def add_kicker(cards: list):
    if 1 in [x[0] for x in cards]:
        return 14
    return score_for_highest(cards, 1)


def check_five(cards: list, size: int, checker):
    card_values = [(card.value, card.suit) for card in cards]
    val = []
    for i in list(itertools.combinations(card_values, size)):
        score = checker(i)
        if 0 < score < 4000 or 7000 < score < 8000:
            pockets = [card_values[i] for i in range(len(cards)) if cards[i].pocket]
            if any(pockets):
                score += add_kicker(pockets)
        val.append(score)
    return max(val)


def check_for_all(cards: list, size: int):
    functions = [check_straight_flush, check_4_of_a_kind, check_full_house, check_flush, check_straight,
                 check_3_of_a_kind, check_2_pair, check_pair, check_high_card]
    for i in functions:
        curr = check_five(cards, size, i)
        if curr:
            return curr
    return 0
