# С клавиатуры вводится натуральное число. Вывести на экран соответсвтующее число элементов ряда Фибоначчи.
#
# Ряд Фибоначчи — это последовательность натуральных чисел,
# где каждое последующее число является суммой двух предыдущих. Например,
# если на ввод поступило число 6, то вывод должен содержать шесть первых чисел ряда Фибоначчи: 1 1 2 3 5 8 13.

x = int(input('Натуральное число: '))
a1 = 1
a2 = 1
a3 = 1
if x>0:
    print(a1)
    for a in range(x):
        print(a3)
        a3 = a1+a2
        a1 = a2
        a2 = a3
else:
    print(x, 'не натуральное')