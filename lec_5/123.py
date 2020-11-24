import sympy
y = sympy.symbols('y')
exp = sympy.sqrt(y)/(y-1)
print(sympy.solveset(exp))
exp = exp.subs(y, 0)
print(exp.evalf())