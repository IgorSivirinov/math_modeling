import sympy
x, y, z, a = sympy.symbols('x y z a')
print(sympy.simplify((x*y**2 - 2*x*y*z + x*z**2 + y**2 - 2*y*z + z**2)/(x**2-1)))
print(sympy.simplify(sympy.sqrt((1+sympy.sin(a))/(1-sympy.sin(a)))+sympy.sqrt((1-sympy.sin(a))/(1+sympy.sin(a)))))