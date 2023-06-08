import numpy as np
import matplotlib.pyplot as plt

datosax, datosay = np.loadtxt("https://raw.githubusercontent.com/lbiedma/anfamaf2022/main/datos/datos3a.dat")

# datosa, y(x) = Cx**A

lendatos = len(datosax)

sumatxcuad = 0
sumaty = 0
sumatxy = 0
sumatx = 0
d = 0
pointsx = []
pointsy = []
aproxy = []

for i in range(lendatos):
    sumatxcuad += np.log(datosax[i])**2
    sumaty += np.log(datosay[i])
    sumatxy += np.log(datosax[i])*np.log(datosay[i])
    sumatx += np.log(datosax[i])

d = lendatos*sumatxcuad-sumatx**2

a0 = np.exp((sumatxcuad*sumaty-sumatxy*sumatx)/d)
a1 = (lendatos*sumatxy-sumatx*sumaty)/d

for k in range(lendatos):
    aproxy.append(a0*datosax[k]**a1)

plt.scatter(datosax,aproxy)
plt.plot(datosax,datosay,color='red')
plt.show()