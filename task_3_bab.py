import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np
fig, ax = plt.subplots()
bab, = plt.plot([],[], '-', color='r', label='Bab')

x = []
y = []

edge = 5
plt.axis('equal')
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)
def animate(t):
    x.append(np.sin(t) * (np.exp(np.cos(t)) - 2 * np.cos(4 * t) + np.sin(t / 12) ** 5))
    y.append(np.cos(t) * (np.exp(np.cos(t)) - 2 * np.cos(4 * t) + np.sin(t / 12) ** 5))
    bab.set_data(x,y)
ani = animation.FuncAnimation(fig, animate,frames=np.arange(0,12*np.pi,0.1),interval=300)
ani.save('t3_bab_3.gif')

