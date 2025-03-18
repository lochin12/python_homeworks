
import numpy as np


vector = np.arange(10, 50)
print("Vector:", vector)


matrix_3x3 = np.arange(9).reshape(3, 3)
print("\n 3x3 Matrix:\n", matrix_3x3)


identity_3x3 = np.eye(3)
print("\n 3x3 Identity Matrix:\n", identity_3x3)


array_3x3x3 = np.random.rand(3, 3, 3)
print("\n 3x3x3 Random Array:\n", array_3x3x3)


array_10x10 = np.random.rand(10, 10)
print("\n Min:", array_10x10.min(), "Max:", array_10x10.max())


vector_30 = np.random.rand(30)
print("\n Mean Value:", vector_30.mean())


matrix_5x5 = np.random.rand(5, 5)
norm_matrix_5x5 = (matrix_5x5 - matrix_5x5.min()) / (matrix_5x5.max() - matrix_5x5.min())
print("\n Normalized 5x5 Matrix:\n", norm_matrix_5x5)


matrix_5x3 = np.random.rand(5, 3)
matrix_3x2 = np.random.rand(3, 2)
print("\n 5x3 * 3x2 Matrix Product:\n", np.dot(matrix_5x3, matrix_3x2))


A = np.random.rand(3, 3)
B = np.random.rand(3, 3)
print("\n Dot Product of Two 3x3 Matrices:\n", np.dot(A, B))


matrix_4x4 = np.random.rand(4, 4)
print("\n Transpose of 4x4 Matrix:\n", matrix_4x4.T)


matrix_3x3 = np.random.rand(3, 3)
print("\n Determinant of 3x3 Matrix:", np.linalg.det(matrix_3x3))


A_3x4 = np.random.rand(3, 4)
B_4x3 = np.random.rand(4, 3)
print("\n Matrix Product (3x4 * 4x3):\n", np.dot(A_3x4, B_4x3))


matrix_3x3 = np.random.rand(3, 3)
vector_3x1 = np.random.rand(3, 1)
print("\n Matrix-Vector Product:\n", np.dot(matrix_3x3, vector_3x1))


A = np.random.rand(3, 3)
b = np.random.rand(3, 1)
x = np.linalg.solve(A, b)
print("\nSolution to Ax = b:\n", x)


matrix_5x5 = np.random.rand(5, 5)
print("\n Row Sums:", matrix_5x5.sum(axis=1))
print("Column Sums:", matrix_5x5.sum(axis=0))
