import sympy
from sympy.solvers.inequalities import reduce_abs_inequality
x = sympy.symbols('x')
expr = sympy.Abs(x**2+2*x-3)+3*(x+1)
print(reduce_abs_inequality(expr,'<',x))
expr = ((x-1)*(x+2))/((x-3)*(x+4))
print(reduce_abs_inequality(expr,'<=',x))