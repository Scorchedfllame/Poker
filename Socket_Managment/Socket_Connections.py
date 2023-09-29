import socket


def server_handshake(port):
    host = ''  # Symbolic name meaning all available interfaces
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(8)
    conn, addr = s.accept()
    conn.sendall(b'server_handshake')
    while True:
        data = conn.recv(1024)
        if data == b'client_handshake':
            return s, conn


def client_handshake(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    data = s.recv(1024)
    if data == b'server_handshake':
        s.sendall(b'client_handshake')
        return s
