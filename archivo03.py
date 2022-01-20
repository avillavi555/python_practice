
#from library01 import *
import library01 as li
import numpy as np
import matplotlib.pyplot as mp
import scipy as sp

a=4.56
b=8.45
#c=suma(a,b)

a,b,f=4.56,8.46,10
#c=suma(a,b)

'''
jj
'''

y=5
li.factFunt(9)
print(np.exp(y**2))

'''
x=np.linspace(-5*np.pi,5*np.pi,1000)
y=np.sin(x**2)
print(x)
mp.xlabel("ejex")
mp.ylabel("eje y")
mp.plot(x,y)
mp.show()
'''

print("xcvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv")

rad = 2
cx = 2
cy = 0
angulo = np.linspace(0, 2*np.pi, 80)
x = rad * np.cos(angulo) + cx
y = rad * np.sin(angulo) + cy

mp.plot(x, y)


mp.title("Circulos")
mp.xlabel("X")
mp.ylabel("Y")
mp.gca().set_aspect('equal')
mp.show()
