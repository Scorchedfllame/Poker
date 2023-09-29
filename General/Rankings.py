from Initialize.Game_Innit import *
from Encoder import *
from random import randint

def rank_hand(hand):
    pass

deck = create_deck()
handTest = [deck[randint(1,13)] for i in range(7)]
print(decode_cards(handTest))
print(handTest)


