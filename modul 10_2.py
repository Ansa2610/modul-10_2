from threading import Thread
from time import sleep


class Knight(Thread):

    def __init__(self, name: str, power: int):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        total_enemies = 100
        number_of_days = 0
        print(f'{self.name}, на нас напали!')
        for i in range(total_enemies):
            if total_enemies > 0:
                total_enemies -= self.power
                number_of_days += 1
                sleep(1)
                print(f'{self.name} сражается {number_of_days} дней (день/дня)..., осталось {total_enemies} воинов.')
                if total_enemies <= 0:
                    print(f'{self.name} одержал победу спустя {number_of_days} дней!')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()   # Запуск потоков
second_knight.start()

first_knight.join()    # остановка текущего
second_knight.join()

print('Все битвы закончились!')
