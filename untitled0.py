import numpy as np 
from scipy.integrate import odeint
import matplotlib.pyplot as plt 

x = np.arange(0, 2, 0.01)
def diff_func(z, x):
    y, omega = z
    
    dy_dt = omega
    domega_d = -np.sin(y) * omega + 3*x*y + 5
    
    return dy_dt, domega_d

omega0 = 0.05
y0 = 0.01
z0 = y0, omega0



sol = odeint(diff_func, z0, x)

plt.plot(x, sol[:,1], 'b')

plt.legend()
plt.show()
