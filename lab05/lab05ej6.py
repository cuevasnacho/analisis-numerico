import numpy as np
import scipy.integrate as integrate

G = 9.8
PI = np.pi

def degrees_to_radians(x):
    x = np.radians(x)
    return x

def pendulo(l,a):
    # funcion #
    a = degrees_to_radians(a)
    f = lambda x: 1/((1-(np.sin(a/2)**2)*(np.sin(x))**2)**(1/2))
    # ------- #

    integral = integrate.quad(f,0,PI/2)
    lg = 4*((l/G)**(1/2))
    t = lg*integral[0]
    return t

p = pendulo(4,45)
print(p)