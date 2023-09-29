from unittest import TestCase
from Initialize.Game_Innit import *
from Server_Managment.Socket_Connections import *


class TestCreateDeck(TestCase):
    def test_first_card(self):
        test_deck = create_deck()
        self.assertEqual("Ace of Spades", test_deck[0])

    def test_last_card(self):
        test_deck = create_deck()
        self.assertEqual("King of Hearts", test_deck[-1])


class TestAddPlayer(TestCase):
    def test_server_reject_player(self):
        player_socket = add_player({'Dan': "test"}, 1000)

    def test_client_reject_player(self):
        s = client_handshake()
        s.sendall(b'notusername:Ben')
        data = s.recv(1024)
        self.assertEqual(data, b'fail')

