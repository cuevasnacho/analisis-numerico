import numpy as np
from lab06ej1 import sumat_sol, sumat_sol_sup

def norma(x,y):
    a = abs(x-y)
    return (max(a))


def jacobi(A,b,err,mit):
    length = len(b)
    u = np.zeros((length,))
    x = np.zeros((length,))

    for k in range(mit):
        for i in range(length):
            u[i] = (b[i] - sumat_sol(A,x,i) - sumat_sol_sup(A,x,i,length))/A[i][i]
        if (norma(u,x) <= err):
            print(f"{u} es la solucion\n")
            break
        for i in range(length):
            x[i] = u[i]
        print(x)
    return x

def gseidel(A,b,err,mit):
    length = len(b)
    u = np.zeros((length,))
    x = np.zeros((length,))

    for k in range(mit):
        for i in range(length):
            u[i] = (b[i] - sumat_sol(A,x,i) - sumat_sol_sup(A,x,i,length))/A[i][i]
        if (norma(u,x) <= err):
            print(f"{u} es la solucion\n")
            break
        for i in range(length):
            x[i] = u[i]
        print(x)
    return x

A = np.array([[3, 1, 1],
              [2, 6, 1],
              [1, 1, 4]])

b = np.array([5, 9, 6])

C = np.array([[5, 7, 6, 5],
              [7, 10, 8, 7],
              [6, 8, 10, 9],
              [5, 7, 9, 10]])

d = np.array([23, 32, 33, 31])

x1 = jacobi(A,b,10e-11,100)
print("\n")
x2 = jacobi(C,d,10e-4,100)