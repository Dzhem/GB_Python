"""
    3. В массиве случайных целых чисел поменять местами минимальный и
    максимальный элементы.
"""

import random


arr = []
ind_max_item = 0
ind_min_item = 0

for i in range(10):
    arr.append(random.randint(0, 100))

    if arr[i] >= arr[ind_max_item]:
        ind_max_item = i

    if arr[i] <= arr[ind_min_item]:
        ind_min_item = i

print('Исходный массив:')
print(*arr)

arr[ind_max_item], arr[ind_min_item] = arr[ind_min_item], arr[ind_max_item]
print('Массив с заменой максимального и минимального элемента:')
print(*arr)
