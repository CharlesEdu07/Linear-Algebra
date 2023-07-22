import numpy as np
import matplotlib.pyplot as plt

units = np.array([1, 2, 3, 4, 5])
price = np.array([1.8, 2.7, 3.4, 3.8, 3.9])

A = np.column_stack((units ** 2, units, np.ones_like(units)))

x = np.linalg.inv(A.T @ A) @ A.T @ price

print("A = ")
print(A)
print("\nb =")
print(price)
print("\nx =")
print(x)

f = x[0] * units ** 2 + x[1] * units + x[2]

plt.plot(units, price, 'bo', label='Data Points')
plt.plot(units, f)
plt.xlabel('Units')
plt.ylabel('Price')
plt.title('Quadratic Fit of Price vs Units')
plt.legend()
plt.show()
