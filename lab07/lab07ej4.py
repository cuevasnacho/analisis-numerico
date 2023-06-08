import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import linprog

costo = np.array([-7,-4,-3])
matriz = np.array([[1,2,2],
                   [2,1,2]])
vector = np.array([30,45])

res = linprog(costo, A_ub=matriz, b_ub=vector, method='simplex')

print(res)