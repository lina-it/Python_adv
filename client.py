# клиент

import psycopg2
import requests
from envparse import Env

env = Env()

DB_URL = env.str("DB_URL")
TOKEN = env.str("TOKEN")

class MyDbClient:
    ORDERS_SELECT_QUERY = "SELECT * FROM orders LIMIT %d"
    ORDER_INSERT_QUERY = "INSERT INTO orders (order_type, description) VALUES ('%s', '%s')"
    ORDER_DELETE_BY_ID_QUERY = "DELETE FROM products WHERE order_id = %d"

    SUBSCRIBE_USER = "INSERT INTO profiles (login, is_subscribed, profile_tg_chat_id) VALUES ('%s', true, %d)"
    UNSUBSCRIBE_USER = "UPDATE profiles SET is_subscribed = false WHERE profile_tg_chat_id = %d"
    GET_SUBSCRIBED_USERS_QUERY = "SELECT * FROM profiles WHERE is_subscribed is true"

    def __init__(self, db_url):
        self.db_url = db_url
        self.connect = None

    def setup(self):
        self.connect = psycopg2.connect(self.db_url)

    def _check_connection(self):
        if not self.connect:
            print("Connection has not been set up! Please, user client.setup method to install connection!")
            return

    def get_orders(self, limit: int) -> list:
        """Получает заданное количество записей из таблица orders"""
        self._check_connection()
        with self.connect.cursor() as cursor:
            cursor.execute(self.ORDERS_SELECT_QUERY % limit)
            return cursor.fetchall()

    def insert_new_product(self, order_type, description, *args, **kwargs):
        """Создаёт заказ в таблице orders"""
        self._check_connection()
        with self.connect.cursor() as cursor:
            cursor.execute(self.ORDER_INSERT_QUERY % (order_type, description))
            self.connect.commit()

    def delete_product_by_id(self, order_id):
        """Удаляет заказ в таблице orders"""
        self._check_connection()
        with self.connect.cursor() as cursor:
            cursor.execute(self.ORDER_DELETE_BY_ID_QUERY % order_id)
            self.connect.commit()

    def subscribe_user_notifications(self, login, profile_tg_chat_id):
        self._check_connection()
        with self.connect.cursor() as cursor:
            cursor.execute(self.SUBSCRIBE_USER % (login, profile_tg_chat_id))
            self.connect.commit()

    def unsubscribe_user_notifications(self, profile_tg_chat_id, login):
        self._check_connection()
        with self.connect.cursor() as cursor:
            cursor.execute(self.UNSUBSCRIBE_USER % profile_tg_chat_id)
            self.connect.commit()

    def get_subcribed_users(self):
        self._check_connection()
        with self.connect.cursor() as cursor:
            cursor.execute(self.GET_SUBSCRIBED_USERS_QUERY)
            return cursor.fetchall()

class MyTgClient:
    def __init__(self, token):
        self.token = token

    def send_text_message(self, message, chat_id):
        requests.get(f"https://api.telegram.org/bot{self.token}/sendMessage?chat_id={chat_id}&text={message}")


class MyApplication:
    def __init__(self, db_client, tg_client):
        self.db_client = db_client
        self.tg_client = tg_client

    def setup_all_components(self):
        self.db_client.setup()

    def create_new_order(self):
        params = dict()
        params['order_type'] = input("Введите тип вопроса: ")
        params['description'] = int(input("Опишите проблему: "))
        self.db_client.insert_new_product(**params)
        message = f"Новая заявка с информацией: {params} создана"
        self.tg_client.send_text_message(message)

    def run(self):
        self.setup_all_components()
        choice_mapper = {
            "q": exit,
            "1": self.create_new_order
        }

        print("Привет! Мы занимаемся ремонтом техники! Введите команду для работы с приложением или q для завершения.")
        print("q - завершить работу с приложением\n"
              "1 - создать заявку")
        while True:
            try:
                user_choice = input("Введите ваш выбор: ")
                choice_mapper[user_choice]()
            except KeyError:
                print("Вы ввели что-то не то, попробуйте ещё раз! ")


# if __name__ == "__main__":
#     my_tg_client = MyTgClient(TOKEN, [362857450, 308251648])
#     my_db_client = MyDbClient(DB_URL)
#     my_application = MyApplication(db_client=my_db_client, tg_client=my_tg_client)
#     my_application.run()