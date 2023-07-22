import numpy as np
import matplotlib.pyplot as plt
import math

t = np.array([0, 1, 2, 3, 4]).T
p = np.array([1000, 1800, 3300, 6000, 11000]).T

A = np.column_stack((t, np.ones_like(t)))
b = np.log(p)

x = np.linalg.inv(A.T @ A) @ A.T @ b

f = x[0] * t + x[1]

plt.plot(t, p, 'bo', label='Data Points')
plt.plot(t, np.exp(f))
plt.xlabel('t')
plt.ylabel('p')
plt.title('Quadratic Fit of t vs p')
plt.legend()
plt.show()

print("f(5) = ", np.exp(x[0] * 5 + x[1]))
