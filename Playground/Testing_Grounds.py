import socket

def mysend(sock, msg):
    totalsent = 0
    MSGLEN = 3
    while totalsent < MSGLEN:
        sent = sock.send(msg[totalsent:])
        if sent == 0:
            raise RuntimeError("socket connection broken")
        totalsent = totalsent + sent

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(("where ever you have your other computer", "port number"))

i = 2
mysend(s, str(i))
