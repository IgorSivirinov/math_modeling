import sympy
from  sympy import sin, cos
x, y, z = sympy.symbols('x y z')
expr = sympy.simplify(sin(x)**2 + cos(x)**2)
print(expr)
expr = sympy.simplify((x**3 + x**2 - x - 1)/(x**2 + 2*x + 1))
print(expr)
print(sympy.expand((x + 1 )**2))
expr = sympy.expand((x + 2 )*(x - 3))
print(expr)
expr = sympy.factor(expr)
print(expr)
expr = sympy.factor(x**3 - x**2 + x - 1)
print(expr)
expr = sympy.expand((cos(x) + sin(x))**2)
print('\n',expr)
expr = sympy.factor((cos(x) + sin(x))**2)
print(expr)

