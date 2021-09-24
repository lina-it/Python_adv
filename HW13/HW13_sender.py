import time

from pika import PlainCredentials, ConnectionParameters, BlockingConnection

connection = BlockingConnection(ConnectionParameters(
               'localhost', credentials=PlainCredentials("rmquser", "rmqpass")))

channel = connection.channel()

import json

product_data = [("а", 1),
                ("б", 2),
                ("в", 3, "г"),
                ("д", 4),
                ("е", 5)]

for _ in range(10):
    for product in product_data:
        d = dict()
        d["description"] = product[0]
        d["quantity"] = product[1]
        channel.basic_publish(exchange='',
                              routing_key='test_queue',
                              body=f'{json.dumps(d)}'.encode())
        print(f" [x] Sent '{d}'")
        time.sleep(.5)

connection.close()
