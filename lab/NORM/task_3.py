import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
frames = 200
G = 9.8
t = np.linspace(0, 5, frames)
k = 12.5

def move_1(variable, t):
    y, v= variable
    dv_dt = v
    d2y_dt2 = G - k/m * y - v*0.2 + 5*np.cos(10*t)
    return dv_dt, d2y_dt2
m = 0.5
v0 = 0.5
y0 = 0.3

variable = y0, v0

def solve_func(i):
    sol = odeint(move_1, variable, t)
    x = np.zeros(len(sol))+0.5
    y = -sol[i, 1]
    return x, y
def solve_func_palk(i):
    sol = odeint(move_1, variable, t)
    x = [(np.zeros(len(sol))+0.5)[i],(np.zeros(len(sol))+0.5)[i]]
    y = [1,-sol[i, 1]]
    return x, y

fig, ax = plt.subplots()

edge = 1
ax.set_xlim(0, edge)
ax.set_ylim(-edge, edge)

ball, = plt.plot([], [], 'o', color='r')
palk, = plt.plot([], [], '-', color='b')
def animate(i):
    ball.set_data(solve_func(i))
    palk.set_data(solve_func_palk(i))

ani = FuncAnimation(fig,
                    animate,
                    frames=frames,
                    interval=30)


ani.save("anim3.gif")
plt.show()