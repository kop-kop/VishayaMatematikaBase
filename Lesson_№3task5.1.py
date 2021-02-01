import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

ax = plt.axes(projection='3d')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

x = np.linspace(-1,1,10)
y = np.linspace(-1,1,10)
X,Y = np.meshgrid(x,y)

#рисуем первую

a,b,c,d = 1,2,3,4
Z = (d - a*X - b*Y) / c
ax.plot_surface(X, Y, Z)

#рисуем вторую

a,b,c,d = 1,2,3,0
Z = (d - a*X - b*Y) / c
ax.plot_surface(X, Y, Z)

plt.show()