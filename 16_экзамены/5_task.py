#  Напишите программу, которая вычисляет число Пи при помощи ряда Эйлера. Количество потоков программы должно определяться параметром командной строки.
import sys
import threading
import math

def calculate_partial_sum(start, end):
    partial_sum = 0
    for k in range(start, end):
        partial_sum += ((-1) ** k) / (2 * k + 1)
    return partial_sum

def calculate_pi(num_threads):
    chunk_size = int(math.ceil(1000000 / num_threads))
    threads = []
    partial_sums = []

    for i in range(num_threads):
        start = i * chunk_size
        end = min((i + 1) * chunk_size, 1000000)
        thread = threading.Thread(target=partial_sums.append, args=(calculate_partial_sum(start, end),))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    pi = sum(partial_sums) * 4

    return pi

if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage: python euler_series.py <num_threads>")
        sys.exit(1)

    num_threads = int(sys.argv[1])

    pi = calculate_pi(num_threads)
    print("Estimated value of pi:", pi)
