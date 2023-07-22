import numpy as np

A = np.array([[-8, 5, -2, 0], [-5, 2, 1, -2], [10, -8, 6, -3], [3, -2, 1, 0]])

D, P = np.linalg.eig(A)

D = np.diag(D)

print(np.round(D, decimals=5))
print("\n")
print(np.round(P, decimals=5))
print("\n")

result1 = np.dot(A, P) - np.dot(P, D)
result2 = np.dot(np.dot(P, D), np.linalg.inv(P))

print(np.round(result1, decimals=5))

print("\n\n")

print(np.round(result2, decimals=5))
