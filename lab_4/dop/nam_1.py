def exponentiation(a:float, n:int):
    out: float = 1
    ind = n
    if n<0:
        ind*=-1
    for i in range(ind):
        out*=a
    if n>=0:
        return out
    else:
        return 1/out
