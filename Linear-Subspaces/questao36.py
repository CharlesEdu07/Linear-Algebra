import numpy as np
from sympy import Matrix, pprint

random_matrix = np.random.randint(10, size=(6, 4))
sympy_matrix = Matrix(random_matrix)
J = sympy_matrix

print("\nMatriz J:\n")

pprint(J)

random_matrix = np.random.randint(10, size=(4, 7))
sympy_matrix = Matrix(random_matrix)
K = sympy_matrix

print("\nMatriz K:\n")

pprint(K)

print("\nMatriz A:\n")

A = J * K

pprint(A)

rref_A = A.rref()

print("\nRREF de A:\n")
pprint(rref_A)

#Definindo espaço das colunas (Colunas pivôs)

print("\nEspaço das colunas:\n")

C = A[:, 0:4]

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