

from threading import Thread
from datetime import datetime
from time import sleep

def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='UTF-8') as file:
        for word in range(word_count):
            file.write(f'Какое-то слово №{word+1}' + '\n')
            sleep(0.1)
        print(f'Завершилась запись в файл {file_name}')

time_start = datetime.now()

write_words(10, "example1.txt")
write_words(30, "example2.txt")
write_words(200, "example3.txt")
write_words(100, "example4.txt")

time_end = datetime.now()
time_res = time_end - time_start
print(f'Время работы функций: {time_res}' + '\n')

time_start2 = datetime.now()

Thd_1 = Thread(target=write_words, args=(10, "example5.txt"))
Thd_2 = Thread(target=write_words, args=(30, "example6.txt"))
Thd_3 = Thread(target=write_words, args=(200, "example7.txt"))
Thd_4 = Thread(target=write_words, args=(100, "example8.txt"))

Thd_1.start()
Thd_2.start()
Thd_3.start()
Thd_4.start()

Thd_1.join()
Thd_2.join()
Thd_3.join()
Thd_4.join()

time_end2 = datetime.now()
time_res2 = time_end2 - time_start2
print(f'Время работы потоков: {time_res2}' + '\n')