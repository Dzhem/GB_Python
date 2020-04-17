"""
Функция находит число из последовательности Фибоначчи
"""
import cProfile


def test_fib(func):
    lst = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    for i, item in enumerate(lst):
        assert item == func(i)
        print(f'Test {i} OK!')


def fib(n):
    if n < 2:
        return n

    return fib(n - 1) + fib(n - 2)


# task_3_fib.fib(10)
# 1000 loops, best of 5: 75 usec per loop

# task_3_fib.fib(15)
# 1000 loops, best of 5: 846 usec per loop

# task_3_fib.fib(20)
# 1000 loops, best of 5: 9.09 msec per loop

cProfile.run('fib(20)')

# cProfile.run('fib(10)') 180 function calls (4 primitive calls) in 0.001 seconds
# cProfile.run('fib(15)') 1976 function calls (4 primitive calls) in 0.007 seconds
# cProfile.run('fib(20)') 21894 function calls (4 primitive calls) in 0.090 seconds

# test_fib(fib)
