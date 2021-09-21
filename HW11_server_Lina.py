import asyncio

DB_URL = 'postgresql://postgres:1111@127.0.0.1:5432/postgres'
UPDATE_False = """UPDATE users SET is_subscribed = 'False' where user_id = (%s)"""

class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    async def handle_echo(self, reader):
        data = await reader.read(1024)  # считывает данные из сокета. writer - для записи в сокет
        message = data.decode()
        conn = psycopg2.connect(DB_URL)
        with conn.cursor() as cursor:
            cursor.execute(UPDATE_False % (f'{message}'))
            # cursor.execute(f"""UPDATE users SET is_subscribed = 'True' where user_id = '{message}';""")
            conn.commit()
        

    def run_server(self):
        """Запускает сервер в вечном цикле"""
        loop = asyncio.get_event_loop()
        coro = asyncio.start_server(client_connected_cb=self.handle_echo, host=self.host, port=self.port,
                                    loop=loop)  # передали параметры
        loop.run_until_complete(coro)

        try:
            loop.run_forever()
        except KeyboardInterrupt:
            print("Server stopped by keyboard")
            loop.close()


serv = Server(host='127.0.0.1', port=5000)
serv.run_server()
