'''
    1. Написать программу, которая будет складывать, вычитать, умножать или делить два числа. Числа и знак операции вводятся пользователем. После выполнения вычисления программа не завершается, а запрашивает новые данные для вычислений. Завершение программы должно выполняться при вводе символа 0 в качестве знака операции. Если пользователь вводит неверный знак (не 0, +, -, *, /), программа должна сообщать об ошибке и снова запрашивать знак операции. Также она должна сообщать пользователю о невозможности деления на ноль, если он ввел его в качестве делителя.
'''

while True:
    num_1 = float(input("Введите первое число: "))
    num_2 = float(input("Введите второе число: "))
    sign = str(input(
        "Введите знак арифметической операции, которую необходимо выполнить над числами или 0 для выхода: "))

    if sign == '0':
        break

    if sign in ("+", "-", "*", "/"):
        if sign == "+":
            print(f"{num_1} {sign} {num_2} = {num_1 + num_2}")
            continue
        if sign == "-":
            print(f"{num_1} {sign} {num_2} = {num_1 - num_2}")
            continue
        if sign == "*":
            print(f"{num_1} {sign} {num_2} = {num_1 * num_2}")
            continue
        if sign == "/" and num_2 != 0:
            print(f"{num_1} {sign} {num_2} = {num_1 / num_2}")
            continue
        else:
            print("На ноль делить нельзя")
            continue
    else:
        print("Введён не верный знак операции. Попробуйте ещё раз.")
        continue