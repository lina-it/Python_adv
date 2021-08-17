# 1. Написать декоратор, который будет печатать на экран время работы функции (пользуемся datetime).

from datetime import datetime
def func_time():
    def outer (func):
        def inner (*args, **kwargs):
            end_time = datetime.now()
#            print("Конец выполнения: ", end_time) # строчка для себя
            print("Время выполнения функции: ", end_time-start_time)
            return func(*args, **kwargs)
        start_time = datetime.now()
#       print("Начало выполнения: ", start_time) # строчка для себя
        return inner
    return outer

@func_time()
def summarizer(n1, n2, n3):
    list_sum = [n1, n2, n3]
    list_sum.sort()
    print("Сумма наибольших двух чисел: ", list_sum[-1] + list_sum[-2])

summarizer(int(input("Первое число: ")), int(input("Второе число: ")), int(input("Третье число: ")))

# 2. Написать функцию для вычислений ряда чисел Фибоначчи (можно через цикл, можно через рекурсию).

def fib(n):
    if n<3:
        return 1
    return fib(n-1) + fib(n-2)
print(fib(int(input("Номер числа Фибоначчи: "))))

# 3. Реализовать функцию, которая принимает три позиционных аргумента и возвращает сумму наибольших двух из них).

def summarizer(n1, n2, n3):
    list_sum = [n1, n2, n3]
    list_sum.sort()
    print("Сумма наибольших двух чисел: ", list_sum[-1] + list_sum[-2])

summarizer(int(input("Первое число: ")), int(input("Второе число: ")), int(input("Третье число: ")))

# или без функции:
n1 = int(input("Первое число: "))
n2 = int(input("Второе число: "))
n3 = int(input("Третье число: "))
list_sum = [n1, n2, n3]
list_sum.sort()
print("Сумма наибольших двух чисел: ", list_sum[-1] + list_sum[-2])