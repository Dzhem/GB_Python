"""
    1. В диапазоне натуральных чисел от 2 до 99 определить,
    сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
    Примечание: 8 разных ответов.
"""

multiplicity = {'2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0}

for _ in range(2, 100):
    if _ % 2 == 0:
        multiplicity['2'] += 1
    if _ % 3 == 0:
        multiplicity['3'] += 1
    if _ % 4 == 0:
        multiplicity['4'] += 1
    if _ % 5 == 0:
        multiplicity['5'] += 1
    if _ % 6 == 0:
        multiplicity['6'] += 1
    if _ % 7 == 0:
        multiplicity['7'] += 1
    if _ % 8 == 0:
        multiplicity['8'] += 1
    if _ % 9 == 0:
        multiplicity['9'] += 1

print('Числа из диапазона 2-99 кратны чифрма от 2 до 9 следующее количество раз:')
for key, val in multiplicity.items():
    print(f'{key}: {val} раз')
