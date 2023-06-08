import numpy as np
import matplotlib.pyplot as plt

def calcula_lineal(a0,a1,x):
    return a1*x+a0

datos = np.loadtxt("https://raw.githubusercontent.com/lbiedma/anfamaf2022/main/datos/datos1a.dat")
datosx = datos[:,0]
datosy = datos[:,1]

lendatos = len(datosx)

sumatxcuad = 0
sumaty = 0
sumatxy = 0
sumatx = 0
d = 0
pointsx = []
pointsy = []
linealx = [0, 5]
linealy = []

for i in range(lendatos):
    sumatxcuad += datosx[i]**2
    sumaty += datosy[i]
    sumatxy += datosx[i]*datosy[i]
    sumatx += datosx[i]

d = lendatos*sumatxcuad-sumatx**2

a0 = (sumatxcuad*sumaty-sumatxy*sumatx)/d
a1 = (lendatos*sumatxy-sumatx*sumaty)/d

for j in range(lendatos):
    pointsx.append(datosx[j])
    pointsy.append(datosy[j])

linealy.append(calcula_lineal(a0,a1,linealx[0]))
linealy.append(calcula_lineal(a0,a1,linealx[1]))

plt.scatter(pointsx,pointsy)
plt.plot(linealx,linealy)
plt.show()