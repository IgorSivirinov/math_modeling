import numpy as np 
from scipy.integrate import odeint
import matplotlib.pyplot as plt 
x = np.arange(-5, 5, 0.01)

def diff_func(z, x):
    y, omega = z
    
    dy_dt = omega
    domega_d = np.sin(x) + np.cos(x)

    return dy_dt, domega_d

y0 = 3
omega0 = 0
z0 = y0, omega0

sol = odeint(diff_func, z0, x)

plt.plot(x, sol[:, 0], 'b')

plt.legend()
plt.show()