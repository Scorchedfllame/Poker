from Initialize.Game_Innit import *

# code doesnt work touch if you dare
# sike code works now


def encode(cards):  # (number, suit) 0=spades, 1=clubs, 2=diamonds, 3=hearts
    suit_conversions = ("Spades", "Clubs", "Diamonds", "Hearts")
    number_conversions = ("bananas", "Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King")
    return [(number_conversions.index(i.split(" ")[0]), suit_conversions.index(i.split(" ")[-1])) for i in cards]


def decode(cards):
    suit_conversions = ("Spades", "Clubs", "Diamonds", "Hearts") #I know its probably bad code to repeat these
    number_conversions = ("bananas", "Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King")
    return [number_conversions[i[0]] + " of " + suit_conversions[i[1]] for i in cards]


