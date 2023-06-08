import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import linprog

costo = np.array([10,8])
matriz = np.array([[-3,-2],
                   [-1,-3],
                   [-8,-2]])
vector = np.array([-3,-1.5,-4])

res = linprog(costo, A_ub=matriz, b_ub=vector)

x = np.linspace(0,1)

y1 = 1.5 - 1.5*x
y2 = 0.5 - (1/3)*x
y3 = 2 - 4*x
y4 = 1 - x

# tomo maximo porque son todas restricciones mayores o iguales a
ymax = np.maximum(y1,np.maximum(y2,y3))

print(res.fun)

plt.fill_between(x,ymax,5,alpha=0.5)
plt.plot(x,y1)
plt.plot(x,y2)
plt.plot(x,y3)
plt.plot(x,y4)
plt.scatter(res.x[0],res.x[1],color='black')

plt.show()