from Initialize.Game_Innit import *
from Client_Managment.Calculations import *
import random

gametime_deck = create_deck()
random.shuffle(gametime_deck)
gametime_deck, hands = deal(2, gametime_deck)
print(hands)
print(gametime_deck)
