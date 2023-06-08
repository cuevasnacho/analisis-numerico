import scipy.integrate as integrate
import numpy as np

def fun_a(x):
    return (np.exp(-x**2))

def fun_b(x):
    return ((x**2)*np.log(x+(x**2+1)**(1/2)))

print(integrate.quad(fun_a,-np.inf,np.inf))
print(integrate.quad(fun_b,0,2))