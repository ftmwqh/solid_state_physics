import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.family']=['sans-serif']
plt.rcParams['font.sans-serif']=['Microsoft YaHei']

a=1
up=1
down=-1
k=np.linspace(down,up,101)
v=np.sin(k*2*np.pi/a*a/2)/np.sqrt(1+(np.cos(k*2*np.pi/a*a/4))**2)

plt.plot(k,v)
plt.xlabel(r"$k_x/\frac{2\pi}{a}$")
plt.ylabel(r"$v_x$")
plt.show()