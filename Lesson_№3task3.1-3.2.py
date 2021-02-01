import matplotlib.pyplot as plt
from numpy import linspace
from math import cos, sin, pi

#координаты центра
x_coor = 10
y_coor = 2

#если a и b равны -> окружность, иначе эллипс
a_const = 6
b_const = 6

#посчитаем расположение каждой точки t эллипса
range_t = linspace(0,2*pi,10000)
x = []
y = []
for t in range_t:
    x_ = a_const * cos(t)
    y_ = b_const * sin(t)
    x.append(x_+x_coor)
    y.append(y_+y_coor)
plt.plot(x, y)

plt.xlabel("x")
plt.ylabel("y")

plt.show()