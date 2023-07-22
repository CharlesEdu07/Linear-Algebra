import numpy as np
import matplotlib.pyplot as plt

velocity = np.array([0, 2, 4, 6, 8, 10])
force = np.array([0, 2.90, 14.8, 39.6, 74.3, 119])

A = np.column_stack([velocity ** 5, velocity ** 4, velocity **
                    3, velocity ** 2, velocity ** 1, velocity ** 0])

a = np.linalg.inv(A) @ force

x = np.linspace(0, 10, 50)
y = np.polyval(a, x)

plt.scatter(velocity, force, color='red', label='Data Points')
plt.plot(x, y, color='blue', label='Interpolating Curve')
plt.xlabel('Velocity (ft/sec)')
plt.ylabel('Force (lb)')
plt.title('Interpolating Polynomial')
plt.legend()
plt.show()

x = 750
y = np.polyval(a, x)

print(f'Forca no projetil a {x:.1f} ft/sec: {y:.2f} lb')