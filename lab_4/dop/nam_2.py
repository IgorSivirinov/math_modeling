def fid(n:int):
    a1 = 1
    a2 = 1
    a3 = 1
    mas = [0, 1, 1]

    if n < 0:
        ind = n * -1
    else:
        ind = n
    for a in range(ind):
        a3 = a1 + a2
        a1 = a2
        a2 = a3
        mas.append(a3)
    if n >= 0:
        return mas[ind]
    else:
        if mas[ind]%2==0:
            return mas[ind]
        else:
            return mas[ind]*-1