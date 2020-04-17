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


def fib_list(n):
    fib_lst = [None] * 1000
    fib_lst[:2] = [0, 1]

    def _fib_list(n):
        if fib_lst[n] is None:
            fib_lst[n] = _fib_list(n - 1) + _fib_list(n - 2)
        return fib_lst[n]

    return _fib_list(n)


# test_fib(fib_list)

# python -m timeit -n 1000 -s "import task_5" "task_5.fib_list(10)"

# "task_5.fib_list(10)"
# 1000 loops, best of 5: 19.6 usec per loop

# "task_5.fib_list(20)"
# 1000 loops, best of 5: 48.3 usec per loop

# "task_5.fib_list(100)"
# 1000 loops, best of 5: 146 usec per loop

# "task_5.fib_list(200)"
# 1000 loops, best of 5: 303 usec per loop

# "task_5.fib_list(500)"
# 1000 loops, best of 5: 838 usec per loop

cProfile.run('fib_list(500)')

# 19/1    0.000    0.000    0.000    0.000 task_5.py:19(_fib_list) - 10
# 39/1    0.000    0.000    0.000    0.000 task_5.py:19(_fib_list) - 20
# 199/1    0.001    0.000    0.001    0.001 task_5.py:19(_fib_list) - 100
# 999/1    0.005    0.000    0.005    0.005 task_5.py:19(_fib_list) - 500
