import numpy as np
from matplotlib import pyplot as plt

data = np.loadtxt("https://raw.githubusercontent.com/lbiedma/anfamaf2022/main/datos/covid_italia.csv",delimiter=",",usecols=1)

m = len(data)

hx = np.arange(1,m+1)
hy = data
x = 0
y = 0
x_cuad = 0
x_y = 0

for i in range(0,m):
    x = x + float((hx[i]))
    y = y + float(np.log(hy[i]))
    x_cuad = x_cuad + (float(hx[i])**2)
    x_y = x_y + float((hx[i])*float(np.log(hy[i])))

# bx + a
a = np.exp(((x_cuad*y)-(x_y*x))/((m*x_cuad)-(x**2)))
b = ((m*x_y)-(x*y))/((m*x_cuad)-(x**2))

hx_new = []
hy_new = []


for k in range(0,m):
    fun = (a*np.exp((b * hx[k])))
    hy_new.append(fun)

plt.plot(hy_new,label="aprox",color="r")
plt.scatter(hx,hy,label="datos",color="g")
plt.legend()
plt.show()