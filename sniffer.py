import socket


s = socket.socket(
    socket.AF_PACKET,
    socket.SOCK_RAW,
    socket.htons(3)
)

s.bind(('eth0',3 ))


while True:
    message = s.recv(1024)
    print(repr(message))