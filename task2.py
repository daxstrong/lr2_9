import timeit


# Исключение для оптимизации хвостовой рекурсии
class TailRecurseException(BaseException):
    def __init__(self, args, kwargs):
        self.args = args
        self.kwargs = kwargs


# Декоратор для хвостовой рекурсии
def tail_recursive(func):
    def wrapper(*args, **kwargs):
        while True:
            try:
                return func(*args, **kwargs)
            except TailRecurseException as e:
                args = e.args
                kwargs = e.kwargs
                continue

    return wrapper


# Рекурсивная функция для вычисления факториала с хвостовой рекурсией
@tail_recursive
def factorial(n, accumulator=1):
    """
    Рекурсивная функция для вычисления факториала.

    Аргументы:
    - n (int): Число для вычисления факториала.
    - accumulator (int): Аккумулятор для промежуточных результатов.

    Возвращает:
    - int: Факториал числа n.
    """
    if n == 0:
        return accumulator
    else:
        raise TailRecurseException((n - 1, n * accumulator), {})


# Рекурсивная функция для вычисления чисел Фибоначчи с хвостовой рекурсией
@tail_recursive
def fib(n, a=0, b=1):
    """
    Рекурсивная функция для вычисления чисел Фибоначчи.

    Аргументы:
    - n (int): Число в последовательности Фибоначчи.
    - a (int): Первое число в последовательности.
    - b (int): Второе число в последовательности.

    Возвращает:
    - int: n-ное число в последовательности Фибоначчи.
    """
    if n == 0:
        return a
    else:
        raise TailRecurseException((n - 1, b, a + b), {})


# Проверка, что скрипт запущен как основной
if __name__ == '__main__':
    # Оценка времени выполнения функций
    print("Время выполнения рекурсивной функции factorial:", timeit.timeit(lambda: factorial(20), number=10000))
    print("Время выполнения рекурсивной функции fib:", timeit.timeit(lambda: fib(20), number=10000))
