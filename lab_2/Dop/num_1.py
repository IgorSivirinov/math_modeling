import math
print('ax^2+bx+c=0')
a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))

d = b**2 - 4*a*c
if a == 0:
    print('На ноль делить нельзя')
else:
    if(d>0):
        print('Будет два корня.')
        print('x1 =', (-b + math.sqrt(d)) / (2*a))
        print('x2 =', (-b - math.sqrt(d)) / (2 * a))
    elif d == 0:
        print('Будет один корень.')
        print('x =', (-b / (2 * a)))
    else:
        print('Нет корней.')