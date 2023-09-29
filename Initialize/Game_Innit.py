from Server_Managment.Socket_Connections import *
from Server.Classes import *


def create_deck():
    suits = ["Spades", "Clubs", "Diamonds", "Hearts"]
    deck = []
    for i in range(1, 14):
        for y in range(4):
            if i == 1:
                deck.append(f"Ace of {suits[y]}")
            elif i <= 10:
                deck.append(f"{i} of {suits[y]}")
            elif i == 11:
                deck.append(f"Jack of {suits[y]}")
            elif i == 12:
                deck.append(f"Queen of {suits[y]}")
            elif i == 13:
                deck.append(f"King of {suits[y]}")
    return deck


def add_player(players: dict, money):
    player_socket, player_connection, player_address = server_handshake()
    player_username = player_connection.recvfrom(player_address[0])
    if player_username.startswith('username:'):
        username = player_username.removeprefix('username:')
        players[username] = Player(username, player_socket, player_connection, player_address, money)
        player_connection.sendto(player_address, bytes('#'.join(players.keys()), 'ascii'))
    else:
        player_connection.sendto(player_address, b'fail')
    return player_socket
