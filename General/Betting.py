# All calculations and logic for the adding and distribution of the pot
from General.Classes import Player


def make_bet(bet, total_number_of_money) -> (int, int, bool):
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


def fold(current_bet: int, player: Player) -> None:
    player.folded = True


def can_check(current_bet: int, player: Player) -> bool:
    if player.all_in:
        return True
    return player.curr_bet == current_bet


def call(current_bet: int, player: Player) -> bool:
    if current_bet <= 0:
        can_check(current_bet, player)
        return False
    else:
        amount_betting, amount_of_money_left, all_in = make_bet(current_bet, player.money)
        player.all_in = all_in
        player.money = amount_of_money_left
        player.curr_bet += amount_betting
        return True


def raise_bet(current_bet: int, player: Player, raise_amount: int) -> None:
    amount_betting, amount_of_money_left, all_in = make_bet(raise_amount + current_bet, player.money)
    player.all_in = all_in
    player.money = amount_of_money_left
    player.curr_bet += amount_betting
