import sympy
from  sympy.vector import CoordSys3D
N = CoordSys3D('N')

x, y, z = sympy.symbols('x y z')
q1, q2 = sympy.symbols('q1 q2')

E1 = ((q1*x)/(sympy.sqrt((x**2+y**2+z**2)**3)))*N.i\
    +((q1*y)/(sympy.sqrt((x**2+y**2+z**2)**3)))*N.j\
    +((q1*z)/(sympy.sqrt((x**2+y**2+z**2)**3)))*N.k

E2 = ((q2*(x-1))/(sympy.sqrt(((x-1)**2+(y-1)**2+(z-1)**2)**3)))*N.i\
    +((q2*(y-1))/(sympy.sqrt(((x-1)**2+(y-1)**2+(z-1)**2)**3)))*N.j\
    +((q2*(z-1))/(sympy.sqrt(((x-1)**2+(y-1)**2+(z-1)**2)**3)))*N.k

E = E1+E2
E = E.subs(q1, 1)
E = E.subs(q2, -0.5)
E = E.subs(x, 3)
E = E.subs(y, 4)
E = E.subs(z, 5)
print(E.evalf())
E = E.dot(E)
print(E.evalf())
