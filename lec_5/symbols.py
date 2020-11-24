import math
import sympy
print(sympy.sqrt(3))
x,y = sympy.symbols('x y')
expr = x + 2*y
print(expr+x)
print(sympy.sin(x**2) - sympy.exp(-2*x) + sympy.cos(sympy.pi / x))

