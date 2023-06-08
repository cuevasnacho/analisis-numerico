import matplotlib.pyplot as plt
import numpy as np
from scipy import interpolate

datos = np.loadtxt('datos_aeroCBA.dat') # tambien puede ir el url

# [:,0] todos los elementos de la columna 0

# Año   T   TM  Tm  PP  V   RA  SN  TS  FG  TN  GR

years = datos[:,0]
temp_media = datos[:,1]
new_list = []
new_years = []
new_values = []
hx = []

l = len(temp_media)

bool_is_nan = np.isnan(temp_media)
for i in range(l):
    if (not bool_is_nan[i]):
        new_years.append(int(years[i]))
        new_list.append(float(temp_media[i]))

f = interpolate.interp1d(new_years,new_list,kind='cubic',fill_value='extrapolate')

for j in range(1957,2018):
    hx.append(j)
    new_values.append(float(f(j)))

print(new_values)

plt.plot(hx,new_values)
plt.show()