"""
    1. Выполнить логические побитовые операции «И», «ИЛИ» и др. над числами 5 и 6.
    Выполнить над числом 5 побитовый сдвиг вправо и влево на два знака.
"""

x = 5
y = 6

print(f"Побитовое ИЛИ (OR):\t\t\t{x} | {y} = {x | y}")
print(f"Побитовое И (AND):\t\t\t{x} & {y} = {x & y}")
print(f"Исключающее ИЛИ (XOR):\t\t{x} ^ {y} = {x ^ y}")
print(f"Побитовое отрицание (NOT):\t{x} = {~x}")
print("--- Побытовые сдвиги ---")
print(f"Побытовый сдвиг вправо: {x} >> 2 = {x >> 2}")
print(f"Побытовый сдвиг влево: {x} << 2 = {x << 2}")