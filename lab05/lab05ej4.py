from math import ceil
import numpy as np
from lab05ej1 import *
from lab05ej2 import *

# funciones
def fun_a(x):
    return (x*np.exp(-x))

# inciso a
# trapecio
n = ceil((10e4/6)**(1/2))
print(n)
print(trapecio(fun_a,0,1,n))

# simpson
n = ceil((10e4/45)**(1/4))
if (n%2==1):
    n+=1
print(n)
print(simpson(fun_a,0,1,n))