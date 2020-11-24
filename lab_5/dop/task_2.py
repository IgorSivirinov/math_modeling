import sympy
from  sympy.vector import CoordSys3D

N = CoordSys3D('N')

a, b, x= sympy.symbols('a b x')

a = 7*N.i + 2*N.j + 8*N.k
b = -4*N.i + x*N.j + 9*N.k
corner_ab = sympy.acos(a.dot(b) / (a.dot(a)*b.dot(b))) * 57.3
print(corner_ab.evalf())
root = corner_ab - 90
print(sympy.solveset(root, x))