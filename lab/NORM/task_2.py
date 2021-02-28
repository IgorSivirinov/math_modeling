import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(0, 5, 0.11)


def diff_func(variable, t):
    x, y = variable

    X = k1*(a0-x-y)
    Y = k2*(a0-x-y)


    return X, Y


a0 = 25
x0 = 0
y0 = 0

k1 = 0.67
k2 = 0.3

variable = x0, y0

sol = odeint(diff_func, variable, t)

plt.plot(t, sol[:, 1], 'b')
plt.plot(t, sol[:, 0], 'r')

plt.legend()
plt.show()