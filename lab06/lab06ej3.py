import numpy as np
from scipy import linalg
from lab06ej1 import soltrinf, soltrsup
from lab06ej2 import soleg

def mat_prod(m,b):
    length = len(m[0])
    p = np.zeros((length,))
    
    for j in range(length):
        for k in range(length):
            p[j] += m[k][j]*b[k]

    return p

def sollu(A,b):
    p, l, u = linalg.lu(A)
    p = np.transpose(p)
    # p^(-1)xb
    p = mat_prod(p,b)

    y = soltrinf(l,p)
    x = soltrsup(u,y)

    print(f"La solucion es: {x}")

    return x

# ejercicio 4

A = np.array([[4, -1, 0, -1, 0, 0],
              [-1, 4, -1, 0, -1, 0],
              [0, -1, 4, 0, 0, -1],
              [-1, 0, 0, 4, -1, 0],
              [0, -1, 0, -1, 4, -1],
              [0, 0, -1, 0, -1, 4]])

b1 = np.array([1, 1, 1, 0, 0, 0])

b2 = np.array([1, 1, 1, 1, 1, 1])

sollu(A,b1)
soleg(A,b1)
sollu(A,b2)
soleg(A,b2)