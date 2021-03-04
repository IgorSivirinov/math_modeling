import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
frames = 200
G = 9.8
t = np.linspace(0, 5, frames)


def move_func(variable, t):
    x, vX, y, vY = variable
    dxdt = vX
    dv_xdt = 0
    dydt = vY
    dv_ydt = -G
    return dxdt, dv_xdt, dydt, dv_ydt
k1 = 0.5
def move_func_2(variable, t):
    x, vX, y, vY = variable
    dxdt = vX
    dv_xdt =  -k1*vX**2
    dydt = vY
    dv_ydt = -G
    return dxdt, dv_xdt, dydt, dv_ydt
k2= 0.1
def move_func_3(variable, t):
    x, vX, y, vY = variable
    dxdt = vX
    dv_xdt = -k2*vX**2
    dydt = vY
    dv_ydt = -G
    return dxdt, dv_xdt, dydt, dv_ydt

v = 10

alpha = 60 * np.pi / 180

x0 = 0
vX0 = v * np.cos(alpha)

y0 = 0
vY0 = v * np.sin(alpha)

variable = x0, vX0, y0, vY0

def solve_func(i, key):
    sol = odeint(move_func, variable, t)
    print(sol)
    if key == 'point':
        x = sol[i, 0]
        y = sol[i, 2]
    else:
        x = sol[:i, 0]
        y = sol[:i, 2]
    return x, y
def solve_func_2(i, key):
    sol = odeint(move_func_2, variable, t)
    print(sol)
    if key == 'point':
        x = sol[i, 0]
        y = sol[i, 2]
    else:
        x = sol[:i, 0]
        y = sol[:i, 2]
    return x, y

def solve_func_3(i, key):
    sol = odeint(move_func_3, variable, t)
    print(sol)
    if key == 'point':
        x = sol[i, 0]
        y = sol[i, 2]
    else:
        x = sol[:i, 0]
        y = sol[:i, 2]
    return x, y

fig, ax = plt.subplots()

edge = 10
ax.set_xlim(0, edge)
ax.set_ylim(0, edge)

ball, = plt.plot([], [], 'o', color='r')
ball_line, = plt.plot([], [], '-', color='r')

ball_2, = plt.plot([], [], 'o', color='b')
ball_line_2, = plt.plot([], [], '-', color='b')

ball_3, = plt.plot([], [], 'o', color='k')
ball_line_3, = plt.plot([], [], '-', color='k')


def animate(i):
    ball.set_data(solve_func(i, 'point'))
    ball_line.set_data(solve_func(i, 'line'))

    ball_2.set_data(solve_func_2(i, 'point'))
    ball_line_2.set_data(solve_func_2(i, 'line'))

    ball_3.set_data(solve_func_3(i, 'point'))
    ball_line_3.set_data(solve_func_3(i, 'line'))

ani = FuncAnimation(fig,
                    animate,
                    frames=frames,
                    interval=30)
plt.show()
