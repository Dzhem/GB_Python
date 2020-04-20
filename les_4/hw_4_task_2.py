"""
    4. Определить, какое число в массиве встречается чаще всего.
    Вариант 2
"""

import random
import cProfile


def nums_most_common(n):
    arr = [random.randint(0, 10) for _ in range(n)]

    num = arr[0]
    max_frq = 1
    for i in range(n - 1):
        frq = 1
        for k in range(i + 1, n):
            if arr[i] == arr[k]:
                frq += 1
        if frq > max_frq:
            max_frq = frq
            num = arr[i]

    if max_frq > 1:
        return num
    else:
        return 'Все элементы уникальны'

# print(nums_most_common(2))

# Результаты тестирования

# "hw_4_task_2.nums_most_common(10)"
# 1000 loops, best of 5: 61.8 usec per loop

# "hw_4_task_2.nums_most_common(100)"
# 1000 loops, best of 5: 1.73 msec per loop

# "hw_4_task_2.nums_most_common(1000)"
# 1000 loops, best of 5: 150 msec per loop

cProfile.run('nums_most_common(1000)')

# cProfile.run('nums_most_common(10)') - 64 function calls in 0.000 seconds
# cProfile.run('nums_most_common(100)') - 540 function calls in 0.003 seconds
# cProfile.run('nums_most_common(1000)') - 5486 function calls in 0.169 seconds
