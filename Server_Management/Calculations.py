def deal(playercount: int, deck: list):
    hands = []
    for i in range(playercount):
        hands.append(deck[:2])
        deck = deck[2:]
    return deck, hands


def river(deck: list):
    return deck[3:], deck[:3]


def make_bet(bet, total_number_of_money):
    all_in = False
    amount_betting = 0
    amount_of_money_left = 0
    if bet >= total_number_of_money:
        all_in = True
        amount_betting = total_number_of_money
    if bet <= total_number_of_money:
        amount_betting = bet
        amount_of_money_left = total_number_of_money - bet
    return amount_betting, amount_of_money_left, all_in
