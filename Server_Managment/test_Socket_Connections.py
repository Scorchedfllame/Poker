from unittest import TestCase
from Server_Managment.Socket_Connections import *


class TestHandhakeSetup(TestCase):
    def test_server_handshake(self):
        server_socket = server_handshake()
        self.assertTrue(server_socket)
        server_socket[1].close()
        server_socket[0].close()

    def test_client_handshake(self):
        client_socket = client_handshake()
        self.assertTrue(client_socket)
        client_socket.close()


class TestSendReceive(TestCase):
    def test_server_send(self):
        server_socket, connection, address = server_handshake()
        send_info('test', conn=connection, addr=address)
        server_socket.close()

    def test_client_receive(self):
        s = client_handshake()
        data = s.recv(1024).decode('uft-8')
        self.assertEqual(data, b'test')
        s.close()
