import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.family']=['sans-serif']
plt.rcParams['font.sans-serif']=['Microsoft YaHei']

a=1
down=-1
up=1
k=np.linspace(down,up,101)
E1=k**2
E2=(k+2)**2
E3=(k-2)**2

# plt.plot(k,E1,color='b')
# plt.plot(k[0:51],E2[0:51],color='r')
# plt.plot(k[50:101], E3[50:101],color='r')
# plt.xlabel(r"$k/\frac{2\pi}{a}$")
# plt.ylabel(r"E$/\frac{\hbar^2}{2m}(\frac{2\pi}{a})^2$")
# plt.show()

a=1
down=0
up=1
k=np.linspace(down,up,101)
E1=k**2
E2=(k-1)**2+2
E3=(k+1)**2+2
E4=(k-2)**2
E5=k**2+4
E6=(k+2)**2

plt.plot(k,E1,label=r"$E_1$",color='b')
plt.plot(k,E2,label=r"$E_2$",color='r')
plt.plot(k,E3,label=r"$E_3$",color='g')
plt.plot(k,E4,label=r"$E_4$",color='y')
plt.plot(k,E5,label=r"$E_5$",color='c')
plt.plot(k,E6,label=r"$E_6$")
plt.xlabel(r"$k_y/\frac{2\pi}{a}$")
plt.ylabel(r"E$/\frac{\hbar^2}{2m}(\frac{2\pi}{a})^2$")
plt.legend(loc='upper left')
plt.show()

