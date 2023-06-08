import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import linprog

costo = np.array([-25,-20])
matriz = np.array([[3,4],
                   [2,1]])
vector = np.array([25,10])

res = linprog(costo, A_ub=matriz, b_ub=vector, method='simplex')

x = np.linspace(0,5)

y1 = (25/4) - (3/4)*x
y2 = 10 - 2*x

#
ymax = np.minimum(y1,y2)
print(res.x)
print(-res.fun)

plt.fill_between(x,ymax,alpha=0.5)
plt.show()