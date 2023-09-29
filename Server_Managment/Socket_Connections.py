import socket


def server_handshake():
    # Echo server program
    HOST = ''  # Symbolic name meaning all available interfaces
    PORT = 50007  # Arbitrary non-privileged port
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(1)
    conn, addr = s.accept()
    conn.sendall(b'server_handshake')
    while True:
        data = conn.recv(1024)
        if data == b'client_handshake':
            return s, conn, addr


def client_handshake():
    # Echo client program
    HOST = '192.168.1.172'  # The remote host
    PORT = 50007  # The same port as used by the server
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    data = s.recv(1024)
    if data == b'server_handshake':
        s.sendall(b'client_handshake')
        return s


def send_info(data, s=None, conn=None, addr=None):
    if conn is not None and addr is not None:
        conn.sendto(bytes(data, 'utf-8'), addr)
    elif s is not None:
        s.sendall(data)
