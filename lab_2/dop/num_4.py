n = int(input('Натуральное число: '))
d: int = 2
if n==1:
    print(1)
else:
    if n>0:
        while n/d!=1:
            if n%d==0:
                n/=d
                print(d)
            else:
                d+=1
        print(d)
    else:
        print(n, 'не натуральное')