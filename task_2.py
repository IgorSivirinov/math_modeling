import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np
fig, ax = plt.subplots()
ball, = plt.plot([],[], '-', color='r', label='Ball')

def circle_move(vx0, vy0,time):
    R = time/300 + 0.25
    alpha = np.arange(0,2*np.pi,0.1)
    x = R*np.cos(alpha)
    y = R*np.sin(alpha)
    return x,y
edge = 3
plt.axis('equal')
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)
def animate(i):
    ball.set_data(circle_move(vx0=0.01, vy0=0.1,time=i))
ani = animation.FuncAnimation(fig, animate,frames=100,interval=100)
ani.save('9.gif')