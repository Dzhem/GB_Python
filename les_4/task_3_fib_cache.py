"""
Функция находит число из последовательности Фибоначчи
"""
import cProfile
import functools


def test_fib(func):
    lst = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    for i, item in enumerate(lst):
        assert item == func(i)
        print(f'Test {i} OK!')


@functools.lru_cache()
def fib(n):
    if n < 2:
        return n

    return fib(n - 1) + fib(n - 2)


# "task_3_fib_cache.fib(10)"
# 1000 loops, best of 5: 289 nsec per loop

# "task_3_fib_cache.fib(100)"
# 1000 loops, best of 5: 306 nsec per loop

# "task_3_fib_cache.fib(200)"
# 1000 loops, best of 5: 301 nsec per loop

cProfile.run('fib(100)')

# 11/1    0.000    0.000    0.000    0.000 task_3_fib_cache.py:15(fib) 10


