"""
    5. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
"""

num_ch = int(input("Введите номер буквы в алфавите: "))

alf = "abcdefghijklmnopqrstuvwxyz"

if num_ch < 27:
    print(f"Это буква {alf[num_ch - 1]}")
else:
    print("Буквы с таким порядковым номером нет.")