class Player:
    def __init__(self, name, socket, connection):
        self.name = name
        self.socket = socket
        self.connection = connection
        self.money = 0

    def __repr__(self):
        return f'{self.name} connected to {self.connection}'


class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
        self.in_hand = False
