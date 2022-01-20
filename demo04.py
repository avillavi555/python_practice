import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
xdata, ydata = [], []
px, py = [], []
plt.axis('equal')
plt.grid()
ln, = plt.plot([], [], 'go', markersize=15)      #  , 'go', markersize=10
vec, = plt.plot([], [], 'g')
nc = 40

g = 9.8
v, ang = 10, 45
vx = v*np.cos(ang*np.pi/180)
vy = v*np.sin(ang*np.pi/180)

def eqs(U, t):
    dx, dy = U[2], U[3]
    ddx, ddy = 0, -g
    return[dx, dy, ddx, ddy]

U0 = [0, 0, vx, vy]
t = np.linspace(0, 2, nc)

sol = odeint(eqs, U0, t)

def init():
    ax.set_xlim(0, 15)
    ax.set_ylim(-2, 5)
    ln.set_data([], [])
    vec.set_data([],[])
    return ln, vec

def animacion(i):
    xdata.append(sol[i, 0])
    ydata.append(sol[i, 1])
    #xdata = sol[i, 0]
    #ydata = sol[i, 1]
    ln.set_data(xdata, ydata)

    #px = [0, sol[i, 0]]
    #py = [0, sol[i, 1]]
    px.append([0, sol[i, 0]])
    py.append([0, sol[i, 1]])
    vec.set_data(px, py)
    return ln, vec

ani = FuncAnimation(fig, animacion, frames=nc,
                    init_func=init, interval=10, blit=True)
plt.show()
