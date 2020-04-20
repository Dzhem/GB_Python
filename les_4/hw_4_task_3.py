"""
    4. Определить, какое число в массиве встречается чаще всего.
    Вариант 3
"""
import random
import cProfile


def nums_most_common(n):
    arr = [random.randint(0, 10) for _ in range(n)]
    frq = 0
    result = 0

    for i in arr:
        cur_frq = arr.count(i)
        if cur_frq > frq:
            frq = cur_frq
            result = i

    return result


# print(nums_most_common(10))

# Результаты тестирования

# "hw_4_task_3.nums_most_common(10)"
# 1000 loops, best of 5: 41.4 usec per loop

# "hw_4_task_3.nums_most_common(100)"
# 1000 loops, best of 5: 707 usec per loop

# "hw_4_task_3.nums_most_common(1000)"
# 1000 loops, best of 5: 38.9 msec per loop

cProfile.run('nums_most_common(1000)')

# cProfile.run('nums_most_common(10)') - 69 function calls in 0.000 seconds
# cProfile.run('nums_most_common(100)') - 657 function calls in 0.003 seconds
# cProfile.run('nums_most_common(1000)') - 6519 function calls in 0.169 seconds
