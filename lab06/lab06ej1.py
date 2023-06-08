import numpy as np

# chequea si es singular
def es_singular(A,length):
    det = 1
    i = 0
    while (det != 0 and i<length):
        det *= A[i][i]
        i += 1

    return det == 0

# sumatorias del algoritmo
def sumat_sol(A,x,i):
    sum = 0
    for j in range(i):
        sum += A[i][j]*x[j]

    return sum

def sumat_sol_sup(A,x,i,length):
    sum = 0
    for j in range(i+1,length):
        sum += A[i][j]*x[j]

    return sum

# algoritmos
def soltrinf(A,b):
    length = len(b)
    x = np.zeros((length,),dtype=float)
    if (not es_singular(A,length)):
        for i in range(length):
            x[i] = (b[i] - sumat_sol(A,x,i))/A[i][i]
        #print(f"La solucion es: {x}")
    else:
        print("LA MATRIZ ES SINGULAR")

    return x

def soltrsup(A,b):
    length = len(b)
    x = np.zeros((length,),dtype=float)
    if (not es_singular(A,length)):
        for i in range(length-1,-1,-1):
            x[i] = (b[i] - sumat_sol_sup(A,x,i,length))/A[i][i]
        #print(f"La solucion es: {x}")
    else:
        print("LA MATRIZ ES SINGULAR")

    return x