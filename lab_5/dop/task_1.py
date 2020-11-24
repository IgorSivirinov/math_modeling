import sympy
from  sympy.vector import CoordSys3D

N = CoordSys3D('N')

a, b, c = sympy.symbols('a b c')

a = 4*N.i + 3*N.j + 8*N.k
b = -2*N.i + 8*N.j + 7*N.k
c = -5*N.i - 6*N.j + 12*N.k

corner_ab = sympy.acos(a.dot(b) / (sympy.sqrt(a.dot(a))*sympy.sqrt(b.dot(b)))) * 57.3
corner_ac = sympy.acos(a.dot(c) / (sympy.sqrt(a.dot(a))*sympy.sqrt(c.dot(c)))) * 57.3
corner_bc = sympy.acos(b.dot(c) / (sympy.sqrt(b.dot(b))*sympy.sqrt(c.dot(c)))) * 57.3

print('a^b =',corner_ab.evalf())
print('a^c =',corner_ac.evalf())
print('b^c =',corner_bc.evalf())