import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from math import pi
import numpy as np


cord = (2.20, 1.57)
x = np.linspace(0, pi, 300)
x1, x2 = np.meshgrid(x, x)


def f(x1, x2):
    return -(np.sin(x1) * np.sin(x1**2 / pi)**20 + np.sin(x2) * np.sin(2 * x2**2 / pi)**20)

z = f(x1, x2)

x1_slice = np.linspace(0, pi, 300)
x2_fixed = cord[1]  
z_slice1 = f(x1_slice, x2_fixed)

x2_slice = np.linspace(0, pi, 300)
x1_fixed = cord[0]
z_slice2 = f(x1_fixed, x2_slice)

fig = plt.figure(figsize=(14, 10))

ax1 = fig.add_subplot(2, 2, 1, projection='3d')
surf1 = ax1.plot_surface(x1, x2, z, cmap='viridis', edgecolor='none')
ax1.scatter(cord[0], cord[1], f(cord[0], cord[1]), color='red', s=50, label='Тестовая точка')
ax1.text(cord[0], cord[1], f(cord[0], cord[1]), f'({cord[0]}, {cord[1]}, {f(cord[0], cord[1])})', color='black')
ax1.set_title('1. Поверхность функции f(x1, x2)')
ax1.set_xlabel('x1')
ax1.set_ylabel('x2')
ax1.set_zlabel('f(x1, x2)')
fig.colorbar(surf1, ax=ax1, shrink=0.5, aspect=10)
ax1.legend()
ax1.view_init(elev=30, azim=45)

ax2 = fig.add_subplot(2, 2, 2, projection='3d')
surf2 = ax2.plot_surface(x1, x2, z, cmap='viridis', edgecolor='none')
ax2.scatter(cord[0], cord[1], f(cord[0], cord[1]), color='red', s=50)
ax2.text(cord[0], cord[1], f(cord[0], cord[1]), f'({cord[0]}, {cord[1]}, {f(cord[0], cord[1])})', color='black')
ax2.set_title('2. Вид сверху')
ax2.set_xlabel('x1')
ax2.set_ylabel('x2')
ax2.set_zlabel('f(x1, x2)')
fig.colorbar(surf2, ax=ax2, shrink=0.5, aspect=10)
ax2.view_init(elev=90, azim=-90)

ax3 = fig.add_subplot(2, 2, 3)
ax3.plot(x1_slice, z_slice1, color='darkorange')
ax3.set_title(f'3. f(x1) при x2 = {cord[1]}')
ax3.set_xlabel('x1')
ax3.set_ylabel('f(x1)')

ax4 = fig.add_subplot(2, 2, 4)
ax4.plot(x2_slice, z_slice2, color='darkgreen')
ax4.set_title(f'4. f(x2) при x1 = {cord[0]}')
ax4.set_xlabel('x2')
ax4.set_ylabel('f(x2)')

plt.tight_layout()
plt.show()