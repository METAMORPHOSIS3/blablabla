from math import sqrt

pi = 3.14
shape = input('please, enter a roomshape')
area = 0
if shape == 'треугольник':
    while True:
        a = int(input('please enter first side of a triangle'))
        b = int(input('please enter second side of a triangle'))
        c = int(input('please enter third side of a triangle'))
        if (a + b) <= c or (b + c) <= a or (c + a) <= b:
            print('Чо за дичь ты ввел?! Повтори ввод!')
        else:
            p = (a + b + c) / 2
            area = sqrt(p * (p - a) * (p - b) * (p - c))
            break
    # print(p)
elif shape == 'круг':
    while True:
        r = int(input('enter a radius'))
        if r <= 0:
            print('Чо за дичь ты ввел?! Повтори ввод!')
        else:
            area = pi * r ** 2
            break
elif shape == 'прямоугольник':
    while True:
        a = int(input('enter a first side size'))
        b = int(input('enter a second side size'))
        if a <= 0 or b <= 0:
            print('Чо за дичь ты ввел?! Повтори ввод!')
        else:
            area = a * b
            break

print(f'площадь {shape}а, {area}, кв.м')
# ======================================================================
# name = input("What is your name? ")
# city = input("Where are you from? ")
# print(f"Hello, {name} from {city}! ")
