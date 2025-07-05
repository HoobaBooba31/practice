import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from math import sin, pi

x1 = 0
cord = (2.20, 1.57)

data1 = [[],[],[]]
data2 = [[],[],[]]
data3 = [[],[],[]]

while x1 <= pi:
    x2 = 0
    while x2 <= pi:
        y = -(sin(x1)*pow(sin(x1**2/pi), 20)) - sin(x2)*pow(sin(2*x2**2/pi), 20)
        data1[0].append(x1)
        data1[1].append(x2)
        data1[2].append(y)
        x2 += 0.01
    x1 += 0.01

x1 = 0
x2 = 0
while x1 <= pi:
    y = -(sin(x1)*pow(sin(x1**2/pi), 20)) - sin(cord[1])*pow(sin(2*cord[1]**2/pi), 20)
    data2[0].append(x1)
    data2[1].append(x2)
    data2[2].append(y)
    x1 += 0.01

x1 = 0
x2 = 0
while x2 <= pi:
    y = -(sin(cord[0])*pow(sin(cord[0]**2/pi), 20)) - sin(x2)*pow(sin(2*x2**2/pi), 20)
    data3[0].append(x1)
    data3[1].append(x2)
    data3[2].append(y)
    x2 += 0.01
    

fig = plt.figure(figsize=(12, 10))

ax1 = fig.add_subplot(2, 2, 1, projection='3d')
ax1.scatter(data1[0], data1[1], data1[2], c='red', marker='^')
ax1.view_init(elev=30, azim=45)
ax1.set_xlabel('x1')
ax1.set_ylabel('x2')
ax1.set_zlabel('f(x1,x2)')
ax1.set_title('1. Изометрия')

ax2 = fig.add_subplot(2, 2, 2, projection='3d')
ax2.scatter(data1[0], data1[1], data1[2], c='blue', marker='^')
ax2.view_init(elev=90, azim=90)
ax2.set_xlabel('x1')
ax2.set_ylabel('x2')
ax2.set_zlabel('f(x1,x2)')
ax2.set_title('2. Изометрия(вид сверху)')

ax3 = fig.add_subplot(2, 2, 3)
ax3.plot(data2[0], data2[2])
ax3.set_xlabel('x1')
ax3.set_ylabel('f(x1)')
ax3.set_title(f'3. y = f(x1) при x2 = {cord[1]}')

ax4 = fig.add_subplot(2, 2, 4)
ax4.plot(data3[0], data3[2])
ax4.set_xlabel('x2')
ax4.set_ylabel('f(x2)')
ax4.set_title(f'4. y = f(x2) при x1 = {cord[0]}')

plt.tight_layout()
plt.show()