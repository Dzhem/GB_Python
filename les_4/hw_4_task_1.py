"""
    4. Определить, какое число в массиве встречается чаще всего.
    Вариант 1
"""

import random
import cProfile


def nums_most_common(n):
    arr = []
    dict_items = {}

    for i in range(n):
        arr.append(random.randint(0, 10))

        if arr[i] in dict_items:  # существует ли такой ключ в словаре
            dict_items[arr[i]] += 1
        else:
            dict_items[arr[i]] = 1

    # Определяем максимальное число включений числа
    max_quantity = 0
    for key, val in dict_items.items():
        if val >= max_quantity:
            max_quantity = val

    # Создаём массив наиболее встречаемых значений в исходном массиве
    result = []
    for key, val in dict_items.items():
        if max_quantity == val:
            result.append(key)

    return result

# print(nums_most_common(1000))

# Результаты тестирования

# "hw_4_task_1.nums_most_common(10)"
# 1000 loops, best of 5: 46.5 usec per loop

# "hw_4_task_1.nums_most_common(100)"
# 1000 loops, best of 5: 411 usec per loop

# "hw_4_task_1.nums_most_common(1000)"
# 1000 loops, best of 5: 4.11 msec per loop

cProfile.run('nums_most_common(1000)')

# cProfile.run('nums_most_common(10)') - 74 function calls in 0.000 seconds
# cProfile.run('nums_most_common(100)') - 657 function calls in 0.002 seconds
# cProfile.run('nums_most_common(1000)') - 6473 function calls in 0.020 seconds
