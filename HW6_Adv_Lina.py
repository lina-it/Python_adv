# Реализуйте базовый класс Car.
# У класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и
# 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Реализовать метод для user-friendly вывода информации об автомобиле.
#

class Car:
    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = False

    def go(self):
        return f'{self.name} is started'

    def stop(self):
        return f'{self.name} is stopped'

    def turn_right(self):
        return f'{self.name} is turned right'

    def turn_left(self):
        return f'{self.name} is turned left'

    def show_speed(self):
        return f'The speed of {self.name} is {self.speed}'

    def show_info(self):
        return f"""Название: {self.name}
Цвет: {self.color}
Скорость: {self.speed}
Полиция?: {self.is_police}"""

class TownCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)

    def show_speed(self):
        print(f'The speed of town car {self.name} is {self.speed}')

        if self.speed > 40:
            return f'Speed of {self.name} is higher than allow for town car'
        elif 0 < self.speed <= 40:
            return f'Speed of {self.name} is normal for town car'
        else:
            return f'Is it the real speed?'

class SportCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)


class WorkCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)

    def show_speed(self):
        print(f'The speed of work car {self.name} is {self.speed}')

        if self.speed > 60:
            return f'Speed of {self.name} is higher than allow for work car'
        elif 0 < self.speed <= 60:
            return f'Speed of {self.name} is normal for work car'
        else:
            return f'Is it the real speed?'

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name)
        self.is_police = True

towncar1 = TownCar(speed=70,color='white',name='Ford')
policecar1=PoliceCar(speed=60,color='white', name='Renault', is_police=True)
workcar1 = WorkCar(speed=40,color='black',name='Skoda')
sportcar1 = SportCar(speed=240,color='red',name='BMW')
print(towncar1.show_info())
print(towncar1.show_speed())
print(f'Now {towncar1.go()}, then {towncar1.turn_left()} and {towncar1.stop()}. '
      f'Then again {towncar1.go()}, {towncar1.turn_right()}. But {towncar1.show_speed()}. '
      f'Police on {policecar1.name} see that {towncar1.name} runs on speed {towncar1.speed} and {policecar1.go()}. '
      f'In half a minute both of them ({towncar1.name} and {policecar1.name} stopped. And despite their similar colors - '
      f'{towncar1.color}, they are not friends. What a wonderful story!')
print(policecar1.show_info())
print(workcar1.show_info())
print(workcar1.show_speed())
print(sportcar1.show_info())
print(sportcar1.show_speed())

c = 1