import numpy as np
import matplotlib.pyplot as plt

def calcula_lineal(a0,a1,x):
    return a1*x+a0

datos = np.loadtxt("https://raw.githubusercontent.com/lbiedma/anfamaf2022/main/datos/datos1a.dat")
datosx = datos[:,0]
datosy = datos[:,1]

lendatos = len(datosx)

ones = np.ones(lendatos)
sumatxcuad = np.dot(datosx,datosx)
sumaty = np.dot(datosy,ones)
sumatxy = np.dot(datosx,datosy)
sumatx = np.dot(datosx,ones)
d = lendatos*sumatxcuad-sumatx**2

pointsx = []
pointsy = []
linealx = [0, 5]
linealy = []

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