import sympy
x, y, z = sympy.symbols('x y z')
expr = sympy.sin(x**2) - sympy.exp(-2*x) + sympy.cos(sympy.pi / x)
expr_now = expr.subs(x, sympy.pi)
print(expr_now.evalf())
expr_now = expr.subs(x, x**2)
print(expr_now.evalf())
expr = x**3 + 4*x*y - z
expr_now = expr.subs([(x,2),(y, 4),(z, 0)])
print(expr_now.evalf())