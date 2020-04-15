"""
    4. Определить, какое число в массиве встречается чаще всего.
"""

import random

arr = []
dict_items = {}

for i in range(20):
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
nums_most_common = []
for key, val in dict_items.items():
    if max_quantity == val:
        nums_most_common.append(key)

print('Массив случайных чисел с повторяющимеся элементами:')
print(*arr)

print(f'В данном массиве чаще всего встречаются числа {nums_most_common}.')
