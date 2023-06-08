from cmath import pi
import numpy as np
import matplotlib.pyplot as plt

puntosx = np.linspace(0,4*np.pi,50)
puntosy = []
coefs = []

for i in range(50):
    puntosy.append(np.cos(puntosx[i]))

for j in range(6):
    hy = []
    coefs = np.polyfit(puntosx,puntosy,deg=j)
    for k in range(50):
        hy.append(np.polyval(coefs,puntosx[k]))
    g = f"Polinomio de grado: {j}"
    plt.plot(puntosx,hy,label=g)

plt.legend()
plt.show()