# Задача "Банковские операции":


from random import randint
from time import sleep
import threading

class Bank:
    lock = threading.Lock ()
    def __init__(self):
        self.balance = 0


    def deposit(self):
        for dps in range(100):

            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            dep_rand = randint(50, 500)
            self.balance += dep_rand
            print(f'Пополнение: {dep_rand}. Баланс: {self.balance} ')
            sleep(0.01)

    def take(self):
        for tk in range(100):
            tk_rand = randint(50, 500)
            print(f'Запрос: {tk_rand} ')
            if tk_rand <= self.balance:
                self.balance -= tk_rand
                print(f'Снятие: {tk_rand}. Баланс: {self.balance} ')
            else:
                print(f'! Запрос отклонен. Недостаточно средств. ')
                self.lock.acquire()
            sleep(0.01)
            pass
bk = Bank()

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')