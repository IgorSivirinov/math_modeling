def changer(a: int,b: list):
    a = 2
    b[0] = 'good'
x = 10
l = [1,2]
changer(x, l)
print(x)
print(l)

l = [1,2]
changer(x,l[:])
print(x,l)

def my_func(a=1,b=0):
    return 3*a-b

