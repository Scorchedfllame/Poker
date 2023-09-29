# Echo client program
import socket

HOST = '192.168.1.172'    # The remote host
PORT = 50007              # The same port as used by the server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    data = s.recv(1024)
    s.sendall(b'handshake')
    print(repr(data))
    while True:
        data = s.recv(1024)
        print(repr(data))