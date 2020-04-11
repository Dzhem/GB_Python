"""
    4. Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
    Количество элементов (n) вводится с клавиатуры.
"""

len_seq = abs(int(input("Введите длину последовательности: ")))
second_element = 1
sum_seq = 0

for i in range(len_seq):
    sum_seq += second_element
    second_element /= -2

print(f"Сумма последовательности 1, -0.5, 0.25, -0.125,… до {len_seq} = {sum_seq}")


