import numpy as np
A = np.array([
    [2.0, 1.0, -4.0],
    [1.0, -1.0, 1.0],
    [-1.0, 3.0, -2.0]
], dtype=float)
b = np.array([-7.0, -2.0, 6.0], dtype=float)
n = len(b)
for j in range(n-1):
    if abs(A[j, j]) < 1e-10:
        raise ValueError("Zero pivot encountered!")
    
    for i in range(j+1, n):
        mult = A[i, j] / A[j, j]
        for k in range(j+1, n):
            A[i, k] = A[i, k] - mult * A[j, k]
        b[i] = b[i] - mult * b[j]
        A[i, j] = 0
print("Upper Triangular Matrix A:")
print(A)
print("Modified b:")
print(b)
x = np.zeros(n)
for i in range(n-1, -1, -1):
    for j in range(i+1, n):
        b[i] = b[i] - A[i, j] * x[j]
    x[i] = b[i] / A[i, i]
print("\nSolution:")
print("x =", x)