import matplotlib.pyplot as mp
import numpy as np
from scipy.integrate import odeint
from matplotlib import animation

a, v0=-9.8, 10
nc=50

def eq(R,t):
    return [R[1], a]

R0= [0, v0]
t=np.linspace(0,2,nc)

sol=odeint (eq, R0, t)
Y=sol[:,0]

fig=mp.figure()
ax=mp.axes(xlim=(0,3), ylim=(-1,10))
line, =ax.plot([],[], 'co', markersize=10)

ejex, ejey= [], []

def inicio():
    line.set_data([], [])
    return line,

def animacion(i):
    ejex.append(t[i])
    ejey.append(Y[i])
    #line.set_data(ejex, ejey)
    line.set_data(2, Y[i])
    return line,

anim=animation.FuncAnimation(fig, animacion, init_func=inicio, frames=nc, interval=20, blit=True)

mp.show()
