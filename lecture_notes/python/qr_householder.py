import numpy as np

def Q_householder(A, column):
    (m,n) = A.shape
    x = A[column-1:m, column-1:column]
    e = np.zeros(x.shape)
    e[0,0]=1
    v = x + np.sign(x[0, 0]) * np.linalg.norm(x) * e
    print("v=", v)
    H = np.eye(m)
    H[(column-1):m, (column-1):m] = np.eye(m-(column-1)) - 2 * v @ v.T / (v.T @ v)
    return H

A = np.array([[1, -2, 13],
              [-6, 5, -4],
              [7, -8, 9],
              [-12, 11, -10]])

rankA = np.linalg.matrix_rank(A)
print("A=", A)
print("rank(A)=", rankA)

Q1 = Q_householder(A, column=1)
print("Q1=", Q1)
R1 = Q1 @ A
print("Q1*A=", R1)

Q2 = Q_householder(R1, column=2)
print("Q2=", Q2)
R2 = Q2 @ Q1 @ A
print("Q2*Q1*A=", R2)

Q3 = Q_householder(R2, column=3)
print("Q3=", Q3)
R3 = Q3 @ Q2 @ Q1 @ A
print("Q3*Q2*Q1*A=", R3)


Q = Q1.conj().T @ Q2.conj().T @ Q3.conj().T
print("Q=", Q)



