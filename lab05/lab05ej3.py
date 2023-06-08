import numpy as np
import matplotlib.pyplot as plt
from lab05ej1 import trapecio

def cos(x):
    return (np.cos(x))

def senint():
    xi = np.linspace(0,2*np.pi,14)
    yi = []
    sin = []
    length = len(xi)
    for i in range(length):
        n = 5*i
        yi.append(trapecio(cos,0,xi[i],n))
        sin.append(np.sin(xi[i]))

    return xi,yi,sin

xi,yi,sin = senint()

plt.plot(xi,sin)
plt.scatter(xi,yi,color='red')
plt.show()