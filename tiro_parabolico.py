import numpy as np
import matplotlib.pyplot as mp
import scipy as sp


t=np.linspace(0,2)
g=9.8

v0=5
alfa=30*np.pi/180
vx0=v0*np.cos(alfa)
vy0=v0*np.sin(alfa)

x=[0]
y=[0]


for i in range(1,t.size):
    x.append(x[0]+vx0*t[i])
    y.append(y[0]+vy0*t[i]-0.5*g*t[i]**2)

mp.axis('equal')
mp.ylim(0,1)
mp.plot(x,y)
mp.show()
