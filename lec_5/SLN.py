from sympy import sin,cos,pi,exp
import sympy
x, y, z = sympy.symbols('x y z')
expr = x**2 - 2
print(sympy.solve(expr, x))
expr = sin(x**2) - exp(-2 * x) + cos(pi / x)
print(sympy.solveset(expr,x))
expr = sympy.Eq(x,y)
print(expr)
expr = sympy.Eq(3,1)
print(expr)

system = [x + y + z - 1, x + y + 2*z - 3, x - 2*y + z]
print(sympy.linsolve(system, [x,y,z]))
system = [x**2 + x,x - y]

