import matplotlib.pyplot as plt
from Plot import WIND, CONTOUR, Data


figure = plt.figure()


ax = plt.subplot2grid((3,3),(0,0))
x=CONTOUR(Data("TC"),ax)
plt.colorbar(x, ax=ax, orientation="vertical")
ax.set_title('Temperatur in der ersten Stunde')
ax.set_xlabel('Breitengrad')
ax.set_ylabel('Längengrad')

ax2 = plt.subplot2grid((3,3),(0,1))
y=WIND(Data("U"),Data("V"),Data("W"), ax2)
plt.colorbar(y, ax=ax2, orientation="vertical")
ax2.set_title('Winde in der ersten Stunde')
ax2.set_xlabel('Breitengrad')
ax2.set_ylabel('Längengrad')

plt.show()
