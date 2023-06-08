import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return 0.75*x-0.5

p = [0.75, -0.5]

puntosx = np.linspace(0,10,20)
puntosy = []
linealx = [0, 10]
linealy = [f(linealx[0]),f(linealx[1])]

numeros_random = np.random.randn(20)

for i in range(20):
    puntosy.append(np.polyval(p,puntosx[i])+numeros_random[i])

coefs = np.polyfit(puntosx,puntosy,deg=1)
puntosy_polyfit = []

puntosy_polyfit.append(np.polyval(coefs,linealx[0]))
puntosy_polyfit.append(np.polyval(coefs,linealx[1]))

plt.plot(linealx,puntosy_polyfit,color='green')
plt.plot(linealx,linealy,color='red')
plt.scatter(puntosx,puntosy,color='blue')
plt.show()