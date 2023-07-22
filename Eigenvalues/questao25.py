import numpy as np

A = np.array([[-3, -2, 0], [14, 7, -1], [-6, -3, 1]])

D, P = np.linalg.eig(A)

D = np.diag(D)

print(D)
print("\n")
print(P)
print("\n")

result1 = np.dot(A, P) - np.dot(P, D)
result2 = np.dot(np.dot(P, D), np.linalg.inv(P))

print(result1)

print("\n")

print(result2)