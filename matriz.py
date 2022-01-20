import numpy as np
import matplotlib.pyplot as mp
import scipy as sp

A=np.array([[1,2,-1],[3,4,5]])
#print(A)
#print(A[:,2])

B=np.zeros((4,5))

B[0,0]=2.3
B[1,0]=2.4
B[2,0]=2.5
B[3,0]=2.6
B[3,4]=2.7
'''
print(B[:,0])
print(B[:,1])
print(B[:,2])
print(B[:,3])
print(B[:,4])

print(B[0,:])
print(B[1,:])
print(B[2,:])
print(B[3,:])
'''

print("ddfdfdfdfdf odeint ddfdfdfdfdf")

numCurvas=5
t=np.linspace(0,2)
g=9.8
v0=10
ang = [20*np.pi/180, 30*np.pi/180, 40*np.pi/180, 50*np.pi/180, 60*np.pi/180]
print(ang)
X=np.zeros((t.size, numCurvas))
Y=np.zeros((t.size, numCurvas))
print(X)
print(Y)
for j in range(numCurvas):
    vx0=v0*np.cos(ang[j])
    vy0=v0*np.sin(ang[j])
    X[0,j]=0
    Y[0,j]=0
    for i in range(1, t.size):
        X[i,j]=X[0,j]+vx0*t[i]
        Y[i,j]=Y[0,j]+vy0*t[i]-0.5*g*t[i]**2

mp.ylim(0,5)

mp.plot(X[:,0], Y[:,0])
mp.plot(X[:,1], Y[:,1])
mp.plot(X[:,2], Y[:,2])
mp.plot(X[:,3], Y[:,3])
mp.plot(X[:,4], Y[:,4])

#mp.plot(X[:,:], Y[:,:])
mp.show()
