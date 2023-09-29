from Initialize.Game_Innit import *
from Server_Management.Calculations import *
from Socket_Managment.Socket_Connections import *
from General.Encoder import *
import random


def host():
    players = []
    gametime_deck = decode_cards(create_deck())
    random.shuffle(gametime_deck)
    gametime_deck, hands = deal(2, gametime_deck)
    print(hands)
    print(gametime_deck)
    players.append(server_handshake(50007))
