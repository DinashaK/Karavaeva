# Дана функция calculate(x, y). Напишите программу, которая создает пул из 5 процессов и распределяет в этом пуле вычисление функции на промежутке х от 0 до 1 с шагом 0,1. у равняется 2 всегда.
import multiprocessing

def calculate(args):
    x, y = args
    return x ** y

if __name__ == "__main__":

    pool = multiprocessing.Pool(processes=5)

    x_values = [i * 0.1 for i in range(11)]

    results = pool.map_async(calculate, [(x, 2) for x in x_values])

    results.wait()  

    for x, result in zip(x_values, results.get()):
        print(f"calculate({x}, 2) = {result}")

    pool.close()
