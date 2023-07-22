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
print("\nEspaço das colunas:\n")

C = A[:, 0:2].row_join(A[:, 3]).row_join(A[:, 5])

pprint(C)

#Definindo espaço nulo

print("\nEspaço nulo:\n")

N = A.nullspace()

pprint(N)

#Definindo matriz R

print("\nMatriz R:\n")

aux = np.array(rref_A[0])
non_zero_rows = aux[~np.all(aux == 0, axis=1)]

R = Matrix(non_zero_rows)

pprint(R)

#Definindo matriz M (espaço nulo de At)

print("\nEspaço nulo de At:\n")

At = A.transpose()
M = At.nullspace()

pprint(M)

#Definindo matriz S = [Rt N]

print("\nMatriz S\n")

Rt = R.transpose()

S = Rt.row_join(N[0])
S = S.row_join(N[1])
S = S.row_join(N[2])

pprint(S)

#Definindo matriz T = [C M]

print("\nMatriz T:\n")

T = C.row_join(M[0])

pprint(T)

#T é uma matriz 5x5. Para realizar a junção de C e M, foi necessário que o número de linhas fossem iguais.