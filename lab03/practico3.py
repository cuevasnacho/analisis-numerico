import numpy as np
import matplotlib.pyplot as plt
import math
from scipy import interpolate

# ejercicio 1
def polinomio_basico(x, i, zi): 
    #x es la lista de puntos a interpolar, i es la posicion del i actual, zi es el valor a evaluar
    n = len(x) # cantidad de puntos x
    xi = x[i] # x sub i
    li = 1
    for j in range(0,n):
        if (j != i):
            li = li*((zi-x[j])/(xi-x[j]))
    
    return li

def ilagrange(x, y, z):
    w = []
    n = len(x)
    m = len(z)

    for j in range(0,m):
        sumat = 0
        for i in range(0,n):
            sumat = sumat + (y[i]*polinomio_basico(x,i,z[j]))
    
        w.append(sumat)

    return w

#print(ilagrange([2, 2.5, 4],[0.5, 0.4, 0.25],[1, 2, 3]))


# ejercicio 2
def dif_div(x, y):
    n = len(x)
    c = np.zeros((n,n))
    coefs = [y[0]]
    pol = y[0]

    for h in range(n):
        c[h][0] = y[h]
    
    for j in range(1,n):
        for i in range(n-j):
            c[i][j] = (c[i+1][j-1]-c[i][j-1])/(x[i+j]-x[i])
        coefs.append(c[0][j])
    #print(coefs)

    return coefs

def prod_newton(z,i,x):
    prod = 1
    
    for j in range(i):
        prod = prod * (z-x[j])
    
    return prod

def inewton(x, y, z):
    c = dif_div(x, y)
    n = len(c)
    m = len(z)
    w = []

    for j in range(m):
        sumat = 0
        for i in range(n):
            sumat = sumat + c[i]*prod_newton(z[j],i,x)
        w.append(sumat)

    return w

#print(inewton([2, 2.5, 4],[0.5, 0.4, 0.25],[1, 2, 3]))


# ejercicio 3
def inversa_x():
    z = []
    j = 1
    y = []

    while (j <= 101):
        x = 24/25+j/25
        z.append(x)
        y.append(1/x)
        j += 1

    w = inewton([1, 2, 3, 4, 5],[1, 0.5, 1/3, 0.25, 0.2],z)


    return y, w, z

'''
y, w, z = inversa_x()

plt.plot(z,y)
plt.plot(z,w)
plt.grid(True)
plt.show()
'''


# ejercicio 4

def f(x):
    res = 1/(1+25*x**2)
    return res

def fun_f_ej4():
    i = 0
    h = 2/200
    x = []
    yr = []

    while (i <= 200):
        k = -1 + i*h
        x.append(k)
        yr.append(f(k))
        i += 1

    return x, yr

def pn_ej4(n):
    x = []
    y = []

    for i in range(1,n+1):
        xi = (2*(i-1))/n - 1
        yi = f(xi)
        x.append(xi)
        y.append(yi)

    return x, y

def qn_ej4(n):
    x = []
    y = []

    for i in range(n):
        xi = math.cos(((2*i+1)/(2*n+2))*math.pi)
        yi = f(xi)
        x.append(xi)
        y.append(yi)

    return x, y

def ej4(x,n):
    i_pn, yp = pn_ej4(n)
    i_qn, yq = qn_ej4(n)

    pny = inewton(i_pn,yp,x)
    qny = inewton(i_qn,yq,x)
    
    return pny, qny

def lab3ej4(n):
    x, y = fun_f_ej4()
    pny = []
    qny = []

    plt.plot(x,y)

    for i in range(1,n+1):
        pny, qny = ej4(x, i)
        plt.plot(x,pny)
        plt.plot(x,qny)
    
    return

'''
lab3ej4(0)
plt.grid(True)
plt.axis([-1,1,0,2])
plt.show()
'''

def lab3ej6():
    hx = [-3, -2, -1, 0, 1, 2, 3]
    hy = [1, 2, 5, 10, 5, 2, 1]
    hz = np.arange(-3,3,0.0625)
    new_hy = []
    length = len(hz)

    print(hz)

    new_hy = ilagrange(hx, hy, hz)
    plt.plot(hz, new_hy, 'r', label='lagrange')

    new_hy = inewton(hx, hy, hz)
    plt.plot(hz, new_hy, 'b', label='newton')

    f = interpolate.interp1d(hx, hy, kind='quadratic')
    new_hy = []
    for i in range(length):
        new_hy.append(f(hz[i]))

    plt.plot(hz, new_hy, 'g', label='interp1d')
    plt.legend()
    plt.show()

    return

#lab3ej6()