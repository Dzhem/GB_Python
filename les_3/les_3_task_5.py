"""
    5. В массиве найти максимальный отрицательный элемент.
    Вывести на экран его значение и позицию в массиве.
"""

import random

arr = []

negative_num = None
ind_negative_num = 0

print('Исходный массив:')
for i in range(20):
    arr.append(random.randint(-10, 10))
    print(arr[i], end=' ')

    if arr[i] < 0 and negative_num is None:
        negative_num = arr[i]
        ind_negative_num = i

    if 0 > arr[i] > negative_num:
        negative_num = arr[i]
        ind_negative_num = i

print(f'\nПервый максимальный отрицательный элемент массива = {negative_num}, '
      f'его индекс = {ind_negative_num}')
