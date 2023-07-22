import numpy as np
import matplotlib.pyplot as plt
import math

t = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]).T
p = np.array([0, 8.8, 29.9, 62.0, 104.7, 159.1, 222.0, 294.5, 380.4, 471.1, 571.7, 686.8, 809.2]).T

A = np.column_stack((t ** 3, t ** 2, t, np.ones_like(t)))

x = np.linalg.inv(A.T @ A) @ A.T @ p

f = x[0] * t ** 3 + x[1] * t ** 2 + x[2] * t + x[3]

plt.plot(t, p, 'bo', label='Data Points')
plt.plot(t, f)
plt.xlabel('v')
plt.ylabel('r')
plt.title('Quadratic Fit of r vs v')
plt.legend()
plt.show()

def f(x, t):
    return x[0] * t ** 3 + x[1] * t ** 2 + x[2] * t + x[3]

print(f(x, 4.5))

print(f(x, 4))

velocity = (f(x, 4.5) - f(x, 4)) / 4.5 - 4

print("\nVelocidade quando t = 4.5 = %2f ft/s" % velocity)
