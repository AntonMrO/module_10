#Домашнее задание по теме "Очереди для обмена данными между потоками."
from queue import Queue
from random import randint
import time
import threading

#Создайте 3 класса: Table, Guest и Cafe

class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None

class Guest(threading.Thread):
    def __init__(self, name):
        super ().__init__ ()
        self.name = name

    def run(self):
        time.sleep(randint(3,10))

class Cafe:
    def __init__(self, *tables):
        self.tables = tables
        self.queue = Queue()

    def guest_arrival(self, *guests):
        for guest in guests:
            for table in self.tables:
                if table.guest is None:
                    table.guest = guest
                    table.guest.start()
                    print(f'{table.guest.name} сел за стол номер {table.number}')
                    break       #сброс цикла если гость за столом
            else:
                self.queue.put(guest)       #ставим гостя в очередь
                print(f'{guest.name} в очереди')

    def discuss_guests(self, *guests):  #процесс обслуживания
        while (not self.queue.empty()) or (self.tables is None):
            for table in self.tables:
                if table.guest.is_alive():
                    print(f'{table.guest.name} покушал(-а) и ушёл(ушла)')
                    print(f'Стол номер {table.number} свободен.')
                    table.guest = None
                    if not self.queue.empty():      #проверка очереди
                        table.guest = self.queue.get()
                        print(f'{table.guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}')
                        table.guest.start()
                    time.sleep(0.5)
        else:
            print('\nВсе гости поели и ушли!')



if __name__ == '__main__':
    # Создание столов
    tables = [Table(number) for number in range(1,6)]

    # Имена гостей
    guests_names = ['Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
                    'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra']

    # Создание гостей
    guests = [Guest(name) for name in guests_names]

    # Заполнение кафе столами
    cafe = Cafe(*tables)

    # Приём гостей
    cafe.guest_arrival(*guests)

    # Обслуживание гостей
    cafe.discuss_guests()