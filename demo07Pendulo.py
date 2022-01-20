import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as mp
from matplotlib.animation import FuncAnimation
'''
theta'=w
theta''=-w^2 * sen(theta)
omega=raiz(g/l)
R=(theta,w)
      R0,R1
'''
L = 9.8
omega0_2 = np.sqrt(9.8/L)

theta0,omega0=30*np.pi/180,1

def pendulo( R , t):
    d_theta = R[1]
    dd_theta = -omega0**2*np.sin( R[0] )
    ecuaciones = [ d_theta , dd_theta ]
    return ecuaciones

npuntos = 140
t = np.linspace(0, 10, npuntos)
R = [theta0,omega0]
sol = odeint(pendulo, R, t) #llama el integrador sin friccion
Theta=sol[:,0]

X = L*np.sin(Theta)
Y = 10 - L*np.cos(Theta)
'''
#mp.ylim(0, 1)
#mp.xlim(-1, 1)
mp.axis('equal')
mp.plot(X, Y)
mp.show()
'''
fig, ax = mp.subplots()
xdata, ydata = [], []

mp.grid()
ln, = mp.plot([], [], 'go', markersize=10)      #  , 'go', markersize=10
vec, = mp.plot([], [])

def init():
    ax.set_xlim(-10, 10)
    ax.set_ylim(0, 10)
    ln.set_data([], [])
    vec.set_data([], [])
    return ln, vec

def animacion(i):
    #xdata.append(X[i])
    #ydata.append(Y[i])
    xdata = X[i]
    ydata = Y[i]
    ln.set_data(xdata, ydata)

    vx = [0, X[i]]
    vy = [10, Y[i]]
    vec.set_data(vx, vy)
    return ln, vec

ani = FuncAnimation(fig, animacion, frames=npuntos,
                    init_func=init, interval=80, blit=True)
mp.show()
