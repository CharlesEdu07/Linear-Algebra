import numpy as np
import matplotlib.pyplot as plt
import math

t = np.array([5, 10, 15, 20, 25, 30]).T
d = np.array([30, 83, 126, 157, 169, 190]).T

A = np.column_stack((t, t**2 * np.exp(-0.1 * t)))

x = np.linalg.inv(A.T @ A) @ A.T @ d

print(x)

f = x[0] * t + x[1] * t**2 * np.exp(-0.1 * t)

plt.plot(t, d, 'bo', label='Data Points')
plt.plot(t, f, label='Fit')
plt.xlabel('t')
plt.ylabel('d')
plt.legend()
plt.show()
