import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = Axes3D(fig)

X = np.arange(-4, 4, 0.25)
Y = np.arange(-4, 4, 0.25)
X, Y = np.meshgrid(X, Y)    # x-y 平面的网格
R = np.sqrt(X ** 2 + Y ** 2)
Z = np.sin(R)
ax.plot_surface(X, Y, Z, rstride=1, cstride=1,  cmap=plt.get_cmap('rainbow')) # 3D图的表示
ax.contourf(X, Y, Z, zdir='z', offset=-2,  cmap='rainbow')
ax.set_zlim(-2,2)
plt.show()