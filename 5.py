from math import sqrt

pi = 3.14
shape = input('please, enter a roomshape')
if shape == 'треугольник':
    a = int(input('please enter first side of a triangle'))
    b = int(input('please enter second side of a triangle'))
    c = int(input('please enter third side of a triangle'))
    p = (a + b + c) / 2
    area = sqrt(p * (a - p) * (b - p) * (c - p))
    print(p)
elif shape == 'круг':
    r = int(input('enter a radius'))
    area = pi * r ** 2
elif shape == 'прямоугольник':
    a = int(input('enter a first side size'))
    b = int(input('enter a second side size'))
    area = a * b

print('площадь', shape, "а", area, "кв.м")
