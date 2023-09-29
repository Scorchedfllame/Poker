from Initialize.Game_Innit import *
from Server_Managment.Calculations import *
from Server_Managment.Socket_Connections import *
import random


def host():
    players = []
    gametime_deck = create_deck()
    random.shuffle(gametime_deck)
    gametime_deck, hands = deal(2, gametime_deck)
    print(hands)
    print(gametime_deck)
    server_handshake()
    send_info(players[0], 'yessir')
