import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


nc = 50
theta, omega0=30*np.pi/180, 1

def eq(R,t):
    dtheta=R[1]
    ddtheta=-omega0**2*np.sin(R[0])
    return[dtheta,ddtheta]

R0=[theta, omega0]
t=np.linspace(0,10,nc)

sol=odeint(eq, R0, t)
Theta=sol[:,0]

X=9.8*np.sin(Theta)
Y=10-9.8*np.cos(Theta)
'''
mp.plot(t,Theta)
mp.plot(X,Y)
mp.show()
'''
fig, ax = plt.subplots()
xdata, ydata = [], []
px, py = [], []
plt.axis('equal')
plt.grid()
ln, = plt.plot([], [], 'go', markersize=15)      #  , 'go', markersize=10
vec, = plt.plot([], [], 'g')

def init():
    ax.set_xlim(-10, 10)
    ax.set_ylim(0, 10)
    ln.set_data([], [])
    vec.set_data([],[])
    return ln, vec

def animacion(i):
    xdata=X[i]
    ydata=Y[i]
    ln.set_data(xdata,ydata)

    #px = [0, sol[i, 0]]
    #py = [0, sol[i, 1]]
    px=(0, X[i])
    py=(10, Y[i])
    vec.set_data(px, py)
    return ln, vec

ani = FuncAnimation(fig, animacion, frames=nc,
                    init_func=init, interval=80, blit=True)
plt.show()
