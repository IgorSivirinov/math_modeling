import matplotlib.pyplot as plt
import numpy as np

t = np.arange(-2*np.pi, 2*np.pi, 0.1)
R = 10

x = R * (t - np.sin(t) ** 3)
y = R * (1 - np.cos(t) ** 3)

plt.plot(x, y, ls='-', lw=3)

plt.axis('equal')

plt.show()

x = R * np.sin(t) ** 3
y = R * np.cos(t) ** 3

plt.plot(x, y, ls='-', lw=3)

plt.axis('equal')

plt.show()