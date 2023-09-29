from Socket_Managment.Socket_Connections import *
from Server_Management.Classes import *
import pickle


def add_player(socket, player_connection, data, players):
    player_username = player_connection.recv(1024).decode('utf-8')
    if player_username.startswith('username:'):
        username = player_username.removeprefix('username:')
        player_connection.sendall(pickle.dumps(data))
        players[username] = Player(username, socket, player_connection)
    else:
        player_connection.sendall(bytes('fail', 'utf-8'))


def kick_player(socket, player_connection, players,  player):
    player_connection.sendall(bytes('disconnect', 'utf-8'))
    socket.close()
    player_connection.close()
    players.pop[player]
