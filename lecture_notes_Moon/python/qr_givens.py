import numpy as np

def Q_givens(x1, x2, size, m, n):
    Q = np.eye(size)
    cos_theta = x1 / np.sqrt(x1**2 + x2**2)
    sin_theta = x2 / np.sqrt(x1**2 + x2**2)
    Q[n-1, n-1] = cos_theta
    Q[m-1, m-1] = cos_theta
    Q[m-1, n-1] = -sin_theta
    Q[n-1, m-1] = sin_theta
    return Q

A = np.array([[1, 6, 7, 12],
              [2, 5, 8, 11],
              [13, 4, 9, 10]])
rankA = np.linalg.matrix_rank(A)
print("rank(A)=", rankA)

Q1 = Q_givens(x1=1, x2=2, size=3, m=2, n=1)
print("Q1=", Q1)
R1 = Q1 @ A
print("Q1*A=", R1)

Q2 = Q_givens(x1=R1[0,0], x2=R1[2,0], size=3, m=3, n=1)
print("Q2=", Q2)
R2 = Q2 @ Q1 @ A
print("Q2*Q1*A=", R2)

Q3 = Q_givens(x1=R2[1,1], x2=R2[2,1], size=3, m=3, n=2)
print("Q3=", Q3)
R3 = Q3 @ Q2 @ Q1 @ A
print("Q3*Q2*Q1*A=", R3)

Q = Q1.conj().T @ Q2.conj().T @ Q3.conj().T
print("Q=", Q)



