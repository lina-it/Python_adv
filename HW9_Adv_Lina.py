#Давайте поэкспериментируем с параллельным выполнением задач.
# Напишите функцию, которая внутри себя будет собирать список с числами от 0 до 100_000_000.
# Далее напишите код, который будет последовательно 3 раза вызывать эту функцию
# измерьте получившееся время выполнения с помощью модуля time или datetime.
#
# Далее перепишите код таким образом, чтобы распараллелить трёхкратное выполнение с использованием потоков
# или процессов на свой вкус и добейтесь ускорения работы программы. Измерьте время выполнения и прикрепите
# результаты измерений к получившемуся коду в виде комментария. Желаю удачи!)

#Первый этап
from datetime import datetime
from threading import Thread
start = datetime.now()
num = [x for x in range(100_000_000)]

def schetchik():
    print("Старт!")
    num
    print("Финиш!")

schetchik()
schetchik()
schetchik()

print(f'На выполнение №1 ушло: {datetime.now() - start}')


#Второй этап
from threading import Thread
start2 = datetime.now()
num2 = [x for x in range(100_000_000)]

def schetchik2():
    print("Старт!")
    num2
    print("Финиш!")

th = Thread(target=schetchik2)
th2 = Thread(target=schetchik2)
th3 = Thread(target=schetchik2)
th.start()  # запускаем поток на исполнение
th2.start()
th3.start()
th.join()  # дожидаемся выполнения всех созданных потоков
th2.join()
th3.join()

print(f'На выполнение №2 ушло: {datetime.now() - start2}')
