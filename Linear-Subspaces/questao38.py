from sympy import Matrix, pprint
import numpy as np

#O rank de uma matriz é o número de colunas linearmente independentes da matriz.

def generate_rank_matrix(rank, size):
    A = np.random.randint(low=-10, high=10, size=(size[0], rank))
    B = np.random.randint(low=-10, high=10, size=(rank, size[1]))
    return A.dot(B)

size = (5, 7)
rank_5_matrix = generate_rank_matrix(5, size)
rank_4_matrix = generate_rank_matrix(4, size)
rank_3_matrix = generate_rank_matrix(3, size)

print("Matrix de rank 5:")
print(rank_5_matrix)

print("\nMatrix de rank 4:")
print(rank_4_matrix)

print("\nMatrix de rank 3:")
print(rank_3_matrix)

A1 = Matrix(rank_5_matrix)
A2 = Matrix(rank_4_matrix)
A3 = Matrix(rank_3_matrix)

print("\nRREF de A1:\n")
rref_A1 = A1.rref()
pprint(rref_A1)

print("\nRREF de A2:\n")
rref_A2 = A2.rref()
pprint(rref_A2)

print("\nRREF de A3:\n")
rref_A3 = A3.rref()
pprint(rref_A3)

#Definindo espaço das colunas (Colunas pivôs)
print("\nEspaço das colunas de A1:\n")
C1 = A1[:, 0:5]
pprint(C1)

print("\nEspaço das colunas de A2:\n")
C2 = A2[:, 0:4]
pprint(C2)

print("\nEspaço das colunas de A3:\n")
C3 = A3[:, 0:3]
pprint(C3)

print("\nMatriz R:\n")

aux1 = np.array(rref_A1[0])
aux2 = np.array(rref_A2[0])
aux3 = np.array(rref_A3[0])

non_zero_rows1 = aux1[~np.all(aux1 == 0, axis=1)]
non_zero_rows2 = aux2[~np.all(aux2 == 0, axis=1)]
non_zero_rows3 = aux3[~np.all(aux3 == 0, axis=1)]

R1 = Matrix(non_zero_rows1)
R2 = Matrix(non_zero_rows2)
R3 = Matrix(non_zero_rows3)

pprint(R1)

print("\n")
pprint(R2)

print("\n")
pprint(R3)

#Calculando CR

print("\nCR de A1:\n")
CR1 = C1 * R1
pprint(CR1)

print("\nCR de A2:\n")
CR2 = C2 * R2
pprint(CR2)

print("\nCR de A3:\n")
CR3 = C3 * R3
pprint(CR3)