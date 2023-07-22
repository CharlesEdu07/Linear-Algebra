import numpy as np
import matplotlib.pyplot as plt

A = np.array([[1, 1, 1], [1, 2, 4], [1, 3, 9]])
B = np.array([6, 15, 28])

X = np.linalg.inv(A) @ B

print(X)

a0, a1, a2 = X

print(f'p(t) = {a0} + {a1}t + {a2}t^2')

x = np.linspace(1, 3, 50)
y = a0 + a1 * x + a2 * x**2

plt.scatter([1, 2, 3], [6, 15, 28], color='red', label='Data Points')
plt.plot(x, y, color='blue', label='Interpolating Curve')
plt.xlabel('t')
plt.ylabel('p(t)')
plt.title('Interpolating Polynomial')
plt.legend()
plt.show()

