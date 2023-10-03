from unittest import TestCase
from Socket_Managment.Socket_Connections import *


address = '10.40.19.203'
port = 50007


class TestHandshakeSetup(TestCase):
    def test_server_handshake(self):
        server_socket = server_handshake(port)
        self.assertTrue(server_socket)
        server_socket[1].close()
        server_socket[0].close()

    def test_client_handshake(self):
        client_socket = client_handshake(address, port)
        self.assertTrue(client_socket)
        client_socket.close()


class TestSendReceive(TestCase):
    def test_server_send(self):
        server_socket, connection = server_handshake(port)
        connection.sendall(bytes('test', 'utf-8'))
        server_socket.close()
        connection.close()

    def test_client_receive(self):
        s = client_handshake(address, port)
        data = s.recv(1024).decode('utf-8')
        self.assertEqual(data, 'test')
        s.close()
