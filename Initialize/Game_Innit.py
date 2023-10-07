from General.Classes import *


def create_deck():
    deck = []
    for i in range(2, 15):
        for y in range(4):
            deck.append(Card(i, y))
    return deck
