from practico3 import ilagrange
import matplotlib.pyplot as plt
import numpy as np
import math

def obtiene_coefs(x,y):
	# x = [x1, x2, x3]
	# y = [y1, y2, y3]
	z = [0,1,-1]
	c, ab1, ab2 = ilagrange(x,y,z)
	# ab1 = a+b+c
	ab1 = ab1 - c
	# ab2 = a-b+c
	ab2 = ab2 - c
	a = (ab1+ab2)/2
	b = (ab2-ab1)/2
	return a, b, c

def baskhara(a,b,c):
    discriminante = b**2 - 4*a*c
    x1 = (-b + math.sqrt(b**2 - 4*a*c))/2*a
    x2 = (-b - math.sqrt(b**2 - 4*a*c))/2*a
    return x1, x2

def rinterp(fun, x0, x1, x2, err, mit):
    hx = [x0, x1, x2]
    hy = [fun(x0), fun(x1), fun(x2)]
    error = fun(hx[-1])
    while (mit > 0 and error < err):
        a, b, c = obtiene_coefs(hx, hy)
        r1, r2 = baskhara(a, b, c)
        r = r1 if (abs(hx[2] - r1) < abs(hx[2] - r2)) else r2
        hx.pop
        hx.append(r)
        mit -= 1
        error = fun(hx[-1])

    return hx[-1]

def fun(x):
    return (x**3 - 2*x + 1/2)

rp = rinterp(fun,-1,0,1,10e-5,100)
print(rp)