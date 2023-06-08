import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import linprog

costo = np.array([-1,-1])
matriz = np.array([[50,24],
                   [30,33]])
vector = np.array([2400,2100])

res = linprog(costo, A_ub=matriz, b_ub=vector)

x = np.linspace(0,70,70)
y = np.linspace(0,70,70)

y1 = 100 - (50/24)*x
y2 = (2100/33) - (30/33)*x

#
ymax = np.minimum(y1,y2)
print(res.x)
print(-res.fun)

# curva de nivel
xmesh, ymesh = np.meshgrid(x,y)
z = xmesh + ymesh

fig, ax = plt.subplots(figsize=(32,32))
ax.set_aspect('equal')
curvas = ax.contour(xmesh, ymesh, z, levels=np.linspace(0, 100, 30))
fig.colorbar(curvas, ax=ax)

plt.fill_between(x,ymax,alpha=0.5)
plt.show()