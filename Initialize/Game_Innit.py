from General.Classes import *


def create_deck():
    deck = []
    for i in range(1, 14):
        for y in range(4):
            deck.append(Card(i, y))
    return deck
