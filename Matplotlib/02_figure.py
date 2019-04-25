import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 50)
y = 2*x + 1
z = x**2

plt.figure()
plt.plot(x, y, color='red', linewidth=1.0, linestyle='--')

plt.figure(num=3, figsize=(8, 5))
plt.plot(x, z)

plt.show()