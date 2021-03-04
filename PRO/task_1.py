import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(0,20, 0.11)


def diff_func(variable, t):
    a, b, c = variable

    A = -k1*a
    B = a*k1-k2*b
    C = b*k2-k3*c
    return A, B, C


a0 = 25
b0 = 0
c0 = 0

k1 = 0.67
k2 = 0.3
k3 = 0.7

variable = a0, b0, c0

sol = odeint(diff_func, variable, t)

plt.plot(t, sol[:, 0], 'b')
plt.plot(t, sol[:, 1], 'r')
plt.plot(t, sol[:, 2], 'k')


plt.legend()
plt.show()