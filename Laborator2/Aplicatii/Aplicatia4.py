import numpy as np
import matplotlib.pyplot as plt

plt.axis([15, 60, 60, 18])
plt.axes().set_aspect('equal')
plt.grid(linestyle=':')

xCentru = 20; yCentru = 20; raza = 40

unghi1 = 20 * np.pi / 180
unghi2 = 70 * np.pi / 180
pas = (unghi2 - unghi1) / 100

xOld = xCentru + raza * np.cos(unghi1)  # coordonatele de inceput
yOld = yCentru + raza * np.sin(unghi1)  # ale arcului

for unghi in np.arange(unghi1 + pas, unghi2, pas):
    x = xCentru + raza * np.cos(unghi)
    y = yCentru + raza * np.sin(unghi)

    plt.plot([xOld, x], [yOld, y], linewidth=5, color='r')

    xOld = x  # memorez ultima coordonata a ultimului punct trasat
    yOld = y  # pt ca de la el sa trasez la urmatorul punct calculat

plt.text(43, 35, '(x1,y1)', fontsize=22)
plt.text(22, 55, '(x2,y2)', fontsize=22)
plt.scatter(xCentru, yCentru, s=50)
plt.text(xCentru - 4, yCentru + 4, '(xC,yC)', fontsize=22)

plt.show()
