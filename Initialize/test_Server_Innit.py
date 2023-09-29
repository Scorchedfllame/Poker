from unittest import TestCase
from Initialize.Server_Innit import *
from Socket_Managment.Socket_Connections import *
import pickle


address = '192.168.1.172'
port = 50007


class TestAddPlayer(TestCase):
    def test_server_reject_player(self):
        player_socket, connection = server_handshake(port)
        add_player(player_socket, connection, 'test')
        player_socket.close()
        connection.close()

    def test_client_reject_player(self):
        s = client_handshake(address, port)
        s.sendall(bytes('notusername:Ben', 'utf-8'))
        data = s.recv(1024).decode('utf-8')
        self.assertEqual(data, 'fail')
        s.close()

    def test_server_add_player(self):
        player_socket, connection = server_handshake(port)
        players = {"Bart": None}
        add_player(player_socket, connection, {1:3, 2:3, 3:3}, players)
        print(players)
        player_socket.close()
        connection.close()

    def test_client_add_player(self):
        s = client_handshake(address, port)
        s.sendall(bytes('username:Ben', 'utf-8'))
        data = s.recv(1024)
        self.assertEqual(pickle.loads(data), {1:3, 2:3, 3:3})
        s.close()
