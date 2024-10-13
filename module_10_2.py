# Домашнее задание по теме "Потоки на классах"

from threading import Thread
from time import sleep

class Knight(Thread):
    war_day = 0
    enemy = 100

    def __init__(self, name, power):
        super().__init__()
        self.name = str(name)
        self.power = int(power)

    def run(self):
        print(f'{self.name}, на нас напали!')
        while self.enemy > 0:
            sleep(1)
            self.war_day += 1
            self.enemy -= self.power
            if self.enemy < 0:      #проверка в случае если power не кратно enemy
                self.enemy = 0      #количество врагов не может быть меньше 0 - устанавливает 0 на посл. цикле
            print(f'{self.name} сражается {self.war_day} дней (дня), осталось {self.enemy} воинов!')
        print(f'{self.name} одержал победу спустя {self.war_day} дней (дня)!\n')

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
Third_knight = Knight("Sir Aragorn", 15)

first_knight.start()
second_knight.start()
Third_knight.start()

first_knight.join()
second_knight.join()
Third_knight.join()
print('Все битвы закончились!')



# Вывод в консоль:
# Sir Lancelot, на нас напали!
# Sir Galahad, на нас напали!
# Sir Aragorn, на нас напали!
# Sir Lancelot сражается 1 дней (дня), осталось 90 воинов!
# Sir Aragorn сражается 1 дней (дня), осталось 85 воинов!
# Sir Galahad сражается 1 дней (дня), осталось 80 воинов!
# Sir Lancelot сражается 2 дней (дня), осталось 80 воинов!
# Sir Galahad сражается 2 дней (дня), осталось 60 воинов!
# Sir Aragorn сражается 2 дней (дня), осталось 70 воинов!
# Sir Lancelot сражается 3 дней (дня), осталось 70 воинов!
# Sir Aragorn сражается 3 дней (дня), осталось 55 воинов!
# Sir Galahad сражается 3 дней (дня), осталось 40 воинов!
# Sir Lancelot сражается 4 дней (дня), осталось 60 воинов!
# Sir Galahad сражается 4 дней (дня), осталось 20 воинов!
# Sir Aragorn сражается 4 дней (дня), осталось 40 воинов!
# Sir Lancelot сражается 5 дней (дня), осталось 50 воинов!
# Sir Aragorn сражается 5 дней (дня), осталось 25 воинов!
# Sir Galahad сражается 5 дней (дня), осталось 0 воинов!
# Sir Galahad одержал победу спустя 5 дней (дня)!
#
# Sir Lancelot сражается 6 дней (дня), осталось 40 воинов!
# Sir Aragorn сражается 6 дней (дня), осталось 10 воинов!
# Sir Lancelot сражается 7 дней (дня), осталось 30 воинов!
# Sir Aragorn сражается 7 дней (дня), осталось 0 воинов!
# Sir Aragorn одержал победу спустя 7 дней (дня)!
#
# Sir Lancelot сражается 8 дней (дня), осталось 20 воинов!
# Sir Lancelot сражается 9 дней (дня), осталось 10 воинов!
# Sir Lancelot сражается 10 дней (дня), осталось 0 воинов!
# Sir Lancelot одержал победу спустя 10 дней (дня)!
#
# Все битвы закончились!





