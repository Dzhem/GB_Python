"""
    4. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят,
    и сколько между ними находится букв.
"""

ch_1 = input("Введите первую букву: ")
ch_2 = input("Введите вторую букву: ")

ch_1 = str.lower(ch_1)
ch_2 = str.lower(ch_2)

alf = "abcdefghijklmnopqrstuvwxyz"

ind_ch_1 = str.index(alf, ch_1)
ind_ch_2 = str.index(alf, ch_2)

count_ch = len(alf[ind_ch_1:ind_ch_2]) - 1

print(f"{ch_1} находится на {ind_ch_1 + 1} позиции в алфавите,\n"
      f"{ch_2} находится на {ind_ch_2 + 1} позиции в алфавите.\n"
      f"Количество букв между {ch_1} и {ch_2}: {count_ch}")
