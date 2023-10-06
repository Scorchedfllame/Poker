import itertools


def rank_hand(hand):
    pass


# --Score Card--
# None: Royal Flush -> Highest Straight Flush--
# 13: Straight Flush--
# 13: Four of a Kind--
# 13: Full House--
# 13: Flush--
# 13: Straight--
# 13: Three of a kind--
# 13: Two Pair--
# 13: Pair--
# 13: High Card--
# 13: Kicker--


def check_flush(cards: list):
    if all(i[1] == cards[0][1] for i in cards):
        return score_for_highest(cards, 12)
    return False


def score_for_highest(cards:list, multiplier):
    return max([x[0] for x in cards]) * 10 ** multiplier


def check_straight_flush(cards: list):
    straight = check_straight(cards)
    if check_flush(cards) and straight:
        return straight * 10 ** 8
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
        return 14 * 10 ** 10
    return score_for_highest(cards, 10)


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
        return value * 10 ** 9
    return False


def check_3_of_a_kind(cards: list):
    value = check_n_of_a_kind(3, cards)
    if value:
        return value * 10 ** 5
    return False


def check_pair(cards: list):
    value = check_n_of_a_kind(3, cards)
    if value:
        return value * 10 ** 3
    return False


def check_2_pair(cards: list):
    first, second = check_n_of_a_kind(2, cards)
    if first and second:
        return first * 10 * 4
    return False


def check_full_house(cards: list):
    two = 0
    three = check_n_of_a_kind(3, cards)
    second = check_n_of_a_kind(2, cards, amount=4)
    for i in second:
        if three != i:
            two = i
    if two and three:
        return (three * 10 ** 8) + (two * 10 ** 7)
    return False


def check_high_card(cards: list):
    return score_for_highest(cards, 2)


def add_kicker(cards: list):
    return score_for_highest(cards, 1)


def check_five(cards: list, size: int, checker):
    val = []
    for i in list(itertools.combinations(cards, size)):
        val.append(checker(i))
    return max(val)
