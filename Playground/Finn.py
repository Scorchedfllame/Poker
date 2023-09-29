
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








############
#
# flop = [(6, 4), (12, 3), (1, 1), (10, 4)]
# hand = [(6, 3), (2, 3)]
#
# def score_cards(hand, flop):
#     flop = []
#     hand = []
#     final_score = 0
#     royal_flush = False
#     straight_flush = False
#     four_of_a_kind = False
#     full_house = False
#     flush = False
#     straight = False
#     three_of_a_kind = False
#     two_pair = False
#     pair = False
#     high_card = False
#
#     for i in range(len(flop)):
#         if
#
#     # for i in range(len(flop)):
#     #     if hand[0][0] == flop[i][0]:
#     #         pair = True
#
#     if royal_flush == True:
#         final_score = 9900
#     elif
#
#     return final_score #4028 = (##__ = score of hand) (__## = score of kicker)
#
###############

