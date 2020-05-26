from matrix import Matrix
from vector import Vector

tmatrix = Matrix((5, 5))
tmatrix2 = Matrix([[0.0, 1.0], [1.0, 1.0]])
tmatrix3 = Matrix([[0.0, 1.0, 2.0], [1.0, 1.0, 3.0]], (2, 3))
tmatrix4 = Matrix([[0.0, 1.0, 2.0], [1.0, 1.0, 3.0]], (2, 3))
tmatrix5 = Matrix([[1.0, 2.0, 3.0, 4.0, 5.0],
                   [1.0, 2.0, 3.0, 4.0, 5.0],
                   [1.0, 2.0, 3.0, 4.0, 5.0],
                   [1.0, 2.0, 3.0, 4.0, 5.0],
                   [1.0, 2.0, 3.0, 4.0, 5.0]])
tmatrix6 = Matrix([[5.0, 1.0], [2.0, 3.0], [3.0, 4.0]], (3, 2))
tmatrix7 = Matrix([[1.0, 2.0, 0.0], [4.0, 3.0, -1.0]], (2, 3))

v1 = Vector(5)

print("Start Matrix")
print(v1)
print(tmatrix)
print(tmatrix2)
print(tmatrix3)
print(tmatrix4)
print(tmatrix5)
print(tmatrix6)
print(tmatrix7)

print("Matrix and Matrix :")
print(tmatrix3 + tmatrix4)
print(tmatrix3 - tmatrix4)
print(tmatrix7 * tmatrix6)

print("Matrix and Vector :")
print(tmatrix + v1)
print(tmatrix - v1)
print(tmatrix5 * v1)

print("Matrix and Scalars")
print(tmatrix5 * 5)
print(tmatrix3 / 5)
