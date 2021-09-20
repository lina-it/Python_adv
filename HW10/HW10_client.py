import socket
import json
from host_port import HOST_PORT_PAIR

sock = socket.create_connection(HOST_PORT_PAIR)
file = "file.json"
# m ='{"id": 2, "name": "abc"}'
# decodedRes = m.read().decode('utf-8')
# data = json.load(decodedRes)

with sock:
     while True:
          with open(file, 'r') as f:
               data = json.loads(f.read())
               sock.send(data.encode())

