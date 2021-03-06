"""
Оптимизация функции Фибоначчи
Мемоизация со словарём
"""
import cProfile


def test_fib(func):
    lst = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    for i, item in enumerate(lst):
        assert item == func(i)
        print(f'Test {i} OK!')


def fib_loop(n):
    if n < 2:
        return n

    first, second = 0, 1

    for i in range(2, n + 1):
        first, second = second, second + first

    return second


# test_fib(fib_loop)

# "task_6.fib_loop(10)"
# 1000 loops, best of 5: 2.72 usec per loop

# "task_6.fib_loop(100)"
# 1000 loops, best of 5: 20.2 usec per loop

# "task_6.fib_loop(500)"
# 1000 loops, best of 5: 147 usec per loop

# "task_6.fib_loop(1000)"
# 1000 loops, best of 5: 397 usec per loop

cProfile.run('fib_loop(100)')

# 1    0.000    0.000    0.000    0.000 task_6.py:15(fib_loop) 100
