import numpy as np
import matplotlib.pyplot as mp
import scipy as sp


t=np.linspace(0,2)
g=9.8
print(t)
y=[1.9]
v=[10]
for i in range(1,t.size):
    v.append(v[0]-g*t[i])
    y.append(y[0]+v[0]*t[i]-0.5*g*t[i]**2)

mp.plot(t,y)
mp.plot(t,v)
mp.show()
