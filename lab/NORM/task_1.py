import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
frames = 200
G = 9.8
t = np.linspace(0, 5, frames)


def move_1(variable, t):
    y, v= variable
    dy_dt = v*v
    d2y_dt2 = -G - 1.9*dy_dt
    return dy_dt, d2y_dt2
m = 0.5
v0 = 1
y0 = 0

variable = y0, v0

def solve_func(i):
    sol = odeint(move_1, variable, t)
    x = np.zeros(len(sol))+1
    y = sol[i, 0]
    return x, y

fig, ax = plt.subplots()

edge = 15
ax.set_xlim(0, edge)
ax.set_ylim(0, edge)

ball, = plt.plot([], [], 'o', color='r')

def animate(i):
    ball.set_data(solve_func(i))

ani = FuncAnimation(fig,
                    animate,
                    frames=frames,
                    interval=30)


ani.save("anim1.gif")
plt.show()
