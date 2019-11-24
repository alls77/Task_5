# Написать метод для вычисления факториала и вычислить факториал 3, 5, и 7.

from multiprocessing import Pool

from utils import timer


def factorial(number):
    value = 1
    for item in range(1, number + 1):
        value *= item
    return value


def start_processes(function, data):
    with Pool(len(data)) as pool:
        return pool.map(function, data)


@timer
def main():
    data = [3, 5, 7]

    result = start_processes(factorial, data)
    print(result)


if __name__ == '__main__':
    main()
