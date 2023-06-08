import numpy as np
from lab06ej1 import soltrsup

def egauss(A,b):
    length = len(b)
    U = np.copy(A)
    y = np.copy(b)
    pivot = 0

    for k in range(length):
        for i in range(length):
            pivot = U[i][k]
            for j in range(length):
                if (i<=k):
                    U[i][j] = U[i][j]
                elif (i>k and j<=k):
                    U[i][j] = 0
                else:
                    U[i][j] = U[i][j] - ((pivot*U[k][j])/U[k][k])
            if (i>k):
                y[i] = y[i] - ((pivot*y[k])/U[k][k])            

    return [U,y]

def soleg(A,b):
    [U,y] = egauss(A,b)
    x = soltrsup(U,y)
    print(f"La solucion es: {x}")

    return x