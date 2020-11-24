import sympy
x = sympy.symbols('x')
corns = sympy.solveset(x**2+x+1/x+1/x**2-4)
print('Корни: ')
for i in corns:
    print(i)
print()
E, e, M = sympy.symbols('E e M')
ur = E - e * sympy.sin(E) - M
ur = ur.subs(e, 0.8)
ur = ur.subs(M, 9)
print(sympy.solveset(ur))

