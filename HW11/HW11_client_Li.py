import socket
import psycopg2

class Client:
    def __init__(self, host, port, timeout=None):
        self.host = host
        self.port = port
        self.timeout = timeout

    def _send(self, message):
        with socket.create_connection((self.host, self.port), self.timeout) as sock:
            try:
                sock.sendall(message.encode("utf8"))
                data = sock.recv(1024)
                print(data.decode())
            except socket.timeout:
                print("send data timeout")
            except socket.error as ex:
                print("send data error:", ex)

    def __call__(self, message):
        self._send(message)
        print("Отправка метрики в БД. Событие: использован метод _send.")

client = Client("127.0.0.1", 5000, timeout=15)
user_answer = ""
while True:
    user_answer = input("Выберите функцию и id пользователя, где\n"
                        "t - подписать \n"
                        "f - отписать\n"
                        "Введите информацию в формате:\n"
                        "t1, где t - функция подписки, а 1 - id пользователя.\n")
    client(user_answer)
    
    # user_answer2 = input("Выберите, пожалуйста, функцию :\n"
    #                      "1 - подписать\n"
    #                      "2 - отписать \n"
    #                      "")
    # us_an = print(user_answer2)
    # if user_answer2 == '1':
    #     print("Спасибо за выбор!")
    #     user_answer = input("Введите нужний id для подписки: \n")
    #     client(user_answer)
    # elif user_answer2 == '2':
    #     print("Спасибо за выбор!")
    #     user_answer = input("Введите нужний id для отписки: \n")
    #     client(user_answer)
    # else:
    #     print("Что-то пошло не так...")