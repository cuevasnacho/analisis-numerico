import numpy as np
from lab05ej1 import simpson

def fun(x):
    return (x*np.exp(-x**2))

# regla de simpson simple
def simpson_s(fun,a,b):
    h = (b-a)/6
    c = (a+b)/2
    i = h*(fun(a)+4*fun(c)+fun(b))
    return i

def error_s(fun,a,b):
    c = (a+b)/2
    ab = simpson_s(fun,a,b)
    ac = simpson_s(fun,a,c)
    cb = simpson_s(fun,c,b)

    err = abs(ab-ac-cb)/15
    return err,ac,cb

def s(fun,a,b,err):
    q = 0
    error_c,ac,cb = error_s(fun,a,b)
    c = (a+b)/2
    if (err>error_c):
        q += ac+cb
    else:
        q += s(fun,a,c,err/2)
        q += s(fun,c,b,err/2)

    return q

q = s(fun,0,1,1e-5)
simpson = simpson_s(fun,0,1)

print(simpson,q)