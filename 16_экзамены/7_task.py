# Напишите программу, которая проверяет все числа от 0 на простоту и выводит простые числа на экран по мере нахождения. Числа должны проверяться в различных потоках (или процессах, по выбору студента) Программа должна работать до тех пор, пока ее не остановит пользователь.
import concurrent.futures
import multiprocessing
import time
import sys

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def check_prime_process(start, end):
    results = []
    for num in range(start, end):
        if is_prime(num):
            results.append(num)
    return results

if __name__ == "__main__":
    num_processors = multiprocessing.cpu_count()

    with concurrent.futures.ProcessPoolExecutor(max_workers=num_processors) as executor:
        future_results = []
        chunk_size = 10000
        start_num = 0
        try:
            while True:
                future = executor.submit(check_prime_process, start_num, start_num + chunk_size)
                future_results.append(future)
                start_num += chunk_size

                for future in concurrent.futures.as_completed(future_results):
                    prime_numbers = future.result()
                    for prime_number in prime_numbers:
                        print("Found prime number:", prime_number)
                    future_results.remove(future)
        except KeyboardInterrupt:
            print("Program stopped by user.")
