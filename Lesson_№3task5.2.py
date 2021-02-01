import matplotlib.pyplot as plt
import math

x = []
y = []
y2 = []
p = 5

for i in range(1000):
    x_ = i/100
    x.append(x_)
    y.append(math.sqrt(2*p*x_ ))
    y2.append(-math.sqrt(2*p*x_))

plt.plot(x,y)
plt.plot(x,y2)
plt.xlabel("x")
plt.ylabel("y")

plt.show()