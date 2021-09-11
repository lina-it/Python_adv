# Вам нужно со # Вам нужно создать своего собственного телеграмм-бота. Для бота реализовать следующий набор команд на основе прошлых дз которые будут:
# #
# # - отдавать перечень заявок в определённом статусе (можно выбрать любой) за конкретный день, созданных
# # конкретным сотрудником;
# # - отдавать перечень сотрудников и департаментов, в которых они работают;
# # - отдавать количество заявок в определенном статусе (можно выбрать любой) по дням;
# # - отдавать перечень id заявок и ФИО сотрудников, которые их создали.
# # - получение сотрудника, департамента, заявки по id
# #
# # Так как у нас может быть очень много данных в базе, поэтому все общие выдачи ограничить 5ю элементами.
#
from telebot import TeleBot
from envparse import Env
from datetime import datetime
import requests
import psycopg2

import db_client_Lina
from db_client_Lina import DbClientV2
from db_client_Lina import DbClient
env = Env()

TOKEN = env.str("TOKEN")
ADMIN_CHAT_ID = 334851749
DB_URL = env.str("DB_URL")

bot = TeleBot(TOKEN)

# обвязка для работы с ботом на сервере телеграмм
bot = TeleBot(TOKEN)
db_client = DbClientV2(DB_URL)
db_client2 = DbClient(DB_URL)
db_client2.setup()
db_client.setup()


def select_orders5(self):
    with self.connect.cursor() as cursor:
        return cursor.fetch(self.SELECT_QUERY1)

@bot.message_handler(commands=["get_chat_id"])
def get_chat_id(message):
    params = message.text.split()[1:]
    print(
        f"Я получил новое сообщение из чата {message.chat.id} от {message.from_user.username} с параметрами: {params}")
    msg_for_user = f"Я общаюсь с тобой в чате {message.chat.id}"
    bot.reply_to(message, text=msg_for_user)

@bot.message_handler(commands=['select_orders'])
def select_orders1(message):
    params_for_selection = dict()
    params_for_selection['status'] = message.text
    print(f"Запрос статуса заказов")
    msg_for_user = f"Укажите, пожалуйста, статус заказа"
    bot.reply_to(message, text=msg_for_user)
    bot.register_next_step_handler(message, upd_date)

def upd_date(message):
    params_for_selection = dict()
    params_for_selection['updated_dt'] = message.text
    bot.reply_to(message, text="Введите дату обновления заказа: ")
    print("Страшивает дату")
    bot.register_next_step_handler(message, creator_id)

def creator_id(message):
    params_for_selection = dict()
    params_for_selection['creator_id'] = message.text
    bot.reply_to(message, text="Введите id создателя: ")
    print("ID")
    bot.register_next_step_handler(message, final)


def final(message):
    # answer = f"Проверьте, пожалуйста, свой запрос:\n" \
    #          f"Статус заказа: {params_for_selection['status']}\n" \
    #          f"Дата обновления: {params_for_selection['updated_dt']}\n" \
    #          f"ID создателя: {params_for_selection['creator_id']}"
        bot.reply_to(message, DbClient.ss())


bot.polling()

while True:
    try:
        bot.polling()
    except Exception as err:
        log_msg = f"Бот упал ({err}), но не был сломлен, поэтому поднялся вновь: {datetime.now()}\n"
        print(log_msg)
        with open("logfile.txt", "a") as logfile:
            logfile.write(log_msg)
            requests.get(f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={ADMIN_CHAT_ID}&text={log_msg}")


