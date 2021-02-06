import matplotlib.pyplot as plt
#from math import sqrt
from numpy import linspace, sqrt

a_const = 10
b_const = 9

#v1


#y = linspace(-1000, 1000, 1000)
#x, y = meshgrid(x, y)

#-(x^2 / (2^2)) - (y^2 / (sqrt(5)^2)) = 1
#y = sqrt( ((x^2) +4) / (4*sqrt(5))  )
#посчитаем расположение каждой точки t гиперболы

#v2

#plt.contour(x, y, -(x**2 / (a_const**2)) - (y**2 / (b_const**2)), [1], colors='k')
#plt.contour(x, y, (x**2/a_const**2 - y**2/b_const**2) , colors='k')

#v3

#y = (x**2/a_const**2 - y**2/b_const**2)
x = linspace(-1000, 1000, 40000)
y = sqrt((b_const**2) * (((x**2)/(a_const**2))-1))

plt.plot(x,y)
plt.plot(x,-y)

plt.xlabel("x")
plt.ylabel("y")

plt.show()