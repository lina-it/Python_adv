import asyncio
import psycopg2

DB_URL = 'postgresql://postgres:1111@127.0.0.1:5432/postgres'
UPDATE_False = """UPDATE users SET is_subscribed = 'False' where user_id = (%s)"""
UPDATE_True = """UPDATE users SET is_subscribed = 'True' where user_id = (%s)"""

class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    async def handle_echo(self, reader, message):
        data = await reader.read(1024)
        message = data.decode()
        conn = psycopg2.connect(DB_URL)
        with conn.cursor() as cursor:
            if message[0] == 't':
                cursor.execute(UPDATE_True % (f'{message[1]}'))
                conn.commit()
            if message[0] == 'f':
                cursor.execute(UPDATE_False % (f'{message[1]}'))
                conn.commit()

    def run_server(self):
        loop = asyncio.get_event_loop()
        coro = asyncio.start_server(client_connected_cb=self.handle_echo, host=self.host, port=self.port,
                                    loop=loop)
        loop.run_until_complete(coro)

        try:
            loop.run_forever()
        except KeyboardInterrupt:
            print("Server stopped by keyboard")
            loop.close()

serv = Server(host='127.0.0.1', port=5000)
serv.run_server()