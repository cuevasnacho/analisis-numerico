import math
import numpy as np
import matplotlib.pyplot as plt

# ejercicio 1

def rbisec(fun,I,err,mit):
    a = I[0]
    b = I[1]
    u = fun(a)
    v = fun(b)
    e = b - a
    hx = []
    hf = []

    if (math.copysign(1,u) == math.copysign(1,v)):
        print("Pruebe con otro intervalo, los extremos evaluados tienen el mismo signo.")
    else:
        for k in range(1,mit):
            e = e/2
            c = a + e
            w = fun(c)
            #print(k,c,w,e)
            if abs(e) < err:
                break
            if (math.copysign(1,w) != math.copysign(1,u)):
                b = c
                v = w
            else:
                a = c
                u = w

            hx.append(c)
            hf.append(fun(c))

    return hx, hf

# pruebas

def cubo(x):
    result = x**3+3

    return result

def polinomio(x):
    result = x**2 + 5*x - 2

    return result

#x, y = rbisec(polinomio,(-2,2),1e-7,100)


# ejercicio 2

def fun_lab2ej2a(x):
    result = math.tan(x) - 2*x

    return result

#hx, hy = rbisec(fun_lab2ej2a, [0.8,1.4], 1e-5, 100)

def fun_lab2ej2b(x):
    result = x**2 - 3

    return result

#aprox_sqrt_3x, aprox_sqrt_3y = rbisec(fun_lab2ej2b, [1.5,2], 1e-5, 100)

def dibuja2a():
    hx = []
    hy = []
    i = -5
    while (i<=5):
        hx.append(i)
        hy.append(fun_lab2ej2a(i))
        i = i+0.0625
    
    plt.plot(hx,hy)
    plt.grid(True)
    plt.axis([-5,5,-5,5])
    plt.show()
    
def dibuja2b():
    x = range(-5,5)
    plt.plot(x,[fun_lab2ej2b(i) for i in x])
    plt.grid(True)
    plt.scatter([math.sqrt(3)],[0])
    
    plt.show()

# ejercicio 3

def rnewton(fun,x0,err,mit):
    hx = []
    hf = []
    v = fun(x0)[0]
    print(0,x0,v)

    for k in range(1,mit):
        x1 = x0 - (v/(fun(x0)[1]))
        v = fun(x1)[0]
        hx.append(x1)
        hf.append(v)
        print(k,x1,v)
        if abs(x1 - x0) < err:
            break
        x0 = x1
    
    return hx, hf


# ejercicio 4

def raiz_cubica(x):
    a = int(input("a = "))
    result = x**3 - a
    result_derivate = 3*x**2
    
    return result, result_derivate


# ejercicio 5

def ripf(fun,x0,err,mit):
    hx = []
    print(0,x0)
    i = 0
    while (i <= mit):
        p = fun(x0)
        print(i,p)
        if (abs(p-x0) < err):
            break
        i = i+1
        hx.append(x0)
        x0 = p

    return hx


# ejercicio 6

def fun_lab2ej6(x):
    result = 2**(x-1)

    return result

#x0 = 1
#hx = ripf(fun_lab2ej6, x0, 1e-5, 100)


# ejercicio 7

# bisec

def lab2ej7bisec():
    x = 0
    f = lambda y : y - (math.e)**(-(1-x*y)**2)
    hx = []
    hy = []
    p = int(input("Ingrese su precision deseada: "))
    prec = round(1.5/p, p)

    while (x <= 1.5):
        hr, hh = rbisec(f,(0,1.5),10e-5,100)
        hx.append(x)
        hy.append(hr[-1])
        x = x + prec
    
    return hx, hy

#hx, hy = lab2ej7bisec()
#plt.plot(hx,hy)
#plt.grid(True)
#plt.show()

# punto fijo

def lab2ej7ripf():
    x = 0
    g = lambda y : (math.e)**((-(1-x*y)**2))
    hx = []
    hy = []
    p = int(input("Ingrese su precision deseada: "))
    prec = round(1.5/p, p)

    while (x <= 1.5):
        hr = ripf(g,0,1e-5,100)
        hx.append(x)
        hy.append(hr[-1])
        x = x + prec
    
    return hx, hy

hx, hy = lab2ej7ripf()
plt.scatter(hx,hy)
plt.grid(True)
plt.show()

# ejercicio 8

def fun_lab2ej8(x):
    first_derivate = x*(math.cos(x)**(-1))**2-2*math.tan(x)
    second_derivate = 2*x*((math.cos(x)**(-1))**2)*math.tan(x)-(math.cos(x)**(-1))**2

    return first_derivate, second_derivate

def ejercicio8():
    result = rnewton(fun_lab2ej8,1.5,1e-4,100)
    
    return result

def fun_labej8_2(x):
    result = math.tan(x)/(x**2)

    return result

#plt.plot([puntos en x],[puntos f(x)])
#plt.show()
#mirar en lbiedma/anfamaf2021