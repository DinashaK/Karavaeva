# Напишите программу, которая создает нить. Родительская и вновь созданная нити должны распечатать десять строк текста.
import threading

def print_ten_lines(prefix):
    for i in range(10):
        print(f"{prefix} Это строка {i + 1}")

thread = threading.Thread(target=print_ten_lines, args=("Дочерняя нить:",))

thread.start()

print_ten_lines("Главная нить:")

thread.join()
