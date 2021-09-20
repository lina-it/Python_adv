
import socket
from host_port import HOST_PORT_PAIR
from logging import getLogger
import json

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(HOST_PORT_PAIR)
sock.listen(socket.SOMAXCONN)
conn, addr = sock.accept()
conn.settimeout(5)

while True:
    conn, addr = sock.accept()
    conn.settimeout(5)
    with conn, sock:
        while True:
            file = conn.recv(1024)
            logger.error(f"{datetime.now()}, {file}")
            print(file.decode("utf-8"))
            if not file:
                break

