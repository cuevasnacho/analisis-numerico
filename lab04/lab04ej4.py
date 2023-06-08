import numpy as np
import matplotlib.pyplot as plt

datosay = np.loadtxt("https://raw.githubusercontent.com/lbiedma/anfamaf2022/main/datos/covid_italia.csv",delimiter=',',usecols=1)

# datosa, y(x) = ae**bx

lendatos = len(datosay)
puntosx = np.linspace(0,41,42)

sumatxcuad = 0
sumaty = 0
sumatxy = 0
sumatx = 0
d = 0
aproxy = []

for i in range(lendatos):
    sumatxcuad += (puntosx[i])**2
    sumaty += np.log(datosay[i])
    sumatxy += (puntosx[i])*np.log(datosay[i])
    sumatx += (puntosx[i])

d = lendatos*sumatxcuad-sumatx**2

a0 = np.exp((sumatxcuad*sumaty-sumatxy*sumatx)/d)
a1 = (lendatos*sumatxy-sumatx*sumaty)/d

for k in range(lendatos):
    aproxy.append(a0*np.exp(a1*puntosx[k]))

plt.plot(puntosx,aproxy)
plt.scatter(puntosx,datosay,color='red')
plt.show()