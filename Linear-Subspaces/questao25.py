from sympy import Matrix, pprint

A = Matrix([
    [1, 2, 0, 3],
    [0, 0, 0, 0],
    [2, 4, 0, 1],
])

rref_A = A.rref()

pprint(rref_A)

print("\nEspaço nulo")

pprint(A.nullspace())