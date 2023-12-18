import timeit
from functools import lru_cache


# Итеративная версия факториала
def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


# Рекурсивная версия факториала
def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)


# Итеративная версия чисел Фибоначчи
def fib_iterative(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


# Рекурсивная версия чисел Фибоначчи
def fib_recursive(n):
    if n <= 1:
        return n
    else:
        return fib_recursive(n - 1) + fib_recursive(n - 2)


# Декоратор lru_cache для рекурсивных функций
@lru_cache(maxsize=None)
def factorial_recursive_cached(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive_cached(n - 1)


@lru_cache(maxsize=None)
def fib_recursive_cached(n):
    if n <= 1:
        return n
    else:
        return fib_recursive_cached(n - 1) + fib_recursive_cached(n - 2)


# Оценка скорости работы итеративной и рекурсивной версий факториала
print("Factorial Iterative:", timeit.timeit("factorial_iterative(10)", globals=globals(), number=100000))
print("Factorial Recursive:", timeit.timeit("factorial_recursive(10)", globals=globals(), number=1000))
print("Factorial Recursive (Cached):", timeit.timeit("factorial_recursive_cached(10)", globals=globals(), number=1000))

# Оценка скорости работы итеративной и рекурсивной версий чисел Фибоначчи
print("Fibonacci Iterative:", timeit.timeit("fib_iterative(10)", globals=globals(), number=100000))
print("Fibonacci Recursive:", timeit.timeit("fib_recursive(10)", globals=globals(), number=1000))
print("Fibonacci Recursive (Cached):", timeit.timeit("fib_recursive_cached(10)", globals=globals(), number=1000))
