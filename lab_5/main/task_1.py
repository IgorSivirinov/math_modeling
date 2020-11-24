import sympy
q, a, p, z = sympy.symbols('q a p z')
p1 = 2
q1 = 2
a1 = 2

ch = (sympy.exp(z)+sympy.exp(-z))/2
sh = (sympy.exp(z)-sympy.exp(-z))/2

x = (a * sh.subs(z, p))/(ch.subs(z, p)-sympy.cos(q))
x = x.subs(p,q1)
x = x.subs(q,q1)
x = x.subs(a,a1)

y = (a*sympy.sin(p))/(ch.subs(z, p) - sympy.cos(q))
y = y.subs(p,q1)
y = y.subs(q,q1)
y = y.subs(a,a1)

print("x =", x.evalf())
print("y =", y.evalf())
