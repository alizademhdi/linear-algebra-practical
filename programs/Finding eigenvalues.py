import numpy as np

def eig_vals(A: np.matrix, iter: int):
    for i in range(iter):
        q, r = np.linalg.qr(A)
        A = np.dot(r, q)

    elements = np.sort(A.diagonal())

    for i in range(elements.size-1, -1, -1):
        print("{:.2f}".format(round(elements[0,i], 2)), end=" ")

A = np.matrix(input())
eig_vals(A, 1000)
