class Player:
    def __init__(self, name):
        self.name = name
        self.all_in = False
        self.folded = False
        self.money = 0
        self.curr_bet = 0


class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
        self.in_hand = False
