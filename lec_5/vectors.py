import sympy
from  sympy.vector import CoordSys3D

N = CoordSys3D('N')
a, b, c = sympy.symbols('a b c')
v = N.i - 2*N.j
print(v/3)