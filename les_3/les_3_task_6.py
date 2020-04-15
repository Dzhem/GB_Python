"""
    6. В одномерном массиве найти сумму элементов, находящихся между
    минимальным и максимальным элементами. Сами минимальный и максимальный
    элементы в сумму не включать.
"""

import random

arr = []
min_item = max_item = None
ind_min_item = ind_max_item = 0
sum_items = 0

print('Исходный массив:')
for i in range(20):
    arr.append(random.randint(-100, 100))
    print(arr[i], end=' ')

    if i == 0:
        min_item = max_item = arr[i]

    if max_item < arr[i]:
        max_item = arr[i]
        ind_max_item = i
    elif min_item > arr[i]:
        min_item = arr[i]
        ind_min_item = i

print(f'\nМаксимальный элемент = {max_item}, его индекс = {ind_max_item}')
print(f'Минимальный элемент = {min_item}, его индекс = {ind_min_item}')

if ind_max_item > ind_min_item:
    sub_arr = arr[ind_min_item + 1:ind_max_item]
else:
    sub_arr = arr[ind_max_item + 1:ind_min_item]

for item in sub_arr:
    sum_items += item

print(f'Сумма элементов, находящихся между {max_item} и {min_item} = {sum_items}')

