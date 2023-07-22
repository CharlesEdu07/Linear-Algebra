from sympy import Matrix, pprint
import numpy as np

#Definindo a matriz A

A = Matrix([
    [7, -9, -4, 5, 3, -3, -7],
    [-4, 6, 7, -2, -6, -5, 5],
    [5, -7, -6, 5, -6, 2, 8],
    [-3, 5, 8, -1, -7, -4, 8],
    [6, -8, -5, 4, 4, 9, 3]
])

#Escalonando a matriz A

rref_A = A.rref()

print("\nRREF de A:\n")
pprint(rref_A)

#Definindo espaço das colunas (Colunas pivôs)

C = A[:, 0:2].row_join(A[:, 3]).row_join(A[:, 5])

print("\nEspaço das colunas:\n")
pprint(C)

#Definindo matriz R em que as linhas são diferentes de zero

print("\nMatriz R:\n")

aux = np.array(rref_A[0])

non_zero_rows = aux[~np.all(aux == 0, axis=1)]

R = Matrix(non_zero_rows)

pprint(R)

#Calculando CR

print("\nMatriz CR:\n")

CR = C * R

pprint(CR)