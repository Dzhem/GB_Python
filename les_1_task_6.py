"""
    6. По длинам трех отрезков, введенных пользователем, определить возможность
    существования треугольника, составленного из этих отрезков.
    Если такой треугольник существует, то определить,
    является ли он разносторонним, равнобедренным или равносторонним.
"""

a = float(input("Введите длину с стороны a треугольника: "))
b = float(input("Введите длину с стороны b треугольника: "))
c = float(input("Введите длину с стороны c треугольника: "))

max_side = max(a, b, c)

if max_side <= a + b + c - max_side:
    print("Треугольник существует")
    if a == b == c:
        print("Треугольник равносторонний")
    elif (a == b) and (a != c) or (b == c) and (b != a) or (a == c) and (a != b):
        print("Треугольник равнобедренный")
    else:
        print("Треугольник разносторонний")

else:
    print("Треугольника с такими сторонами не существует")
