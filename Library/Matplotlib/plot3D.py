import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits import mplot3d

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
x = y = np.linspace(-5, 5, 1000)
X, Y = np.meshgrid(x, y)
z = (X - Y)**2
print(z.shape)
ax.plot_surface(X, Y, z)

plt.show()
