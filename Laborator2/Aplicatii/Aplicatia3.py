import numpy as np
import matplotlib.pyplot as plt

plt.axis([15, 60, 60, 18])
plt.gca().set_aspect('equal')
plt.grid(linestyle=':')

# Coordonatele centrului și raza
xCentru = 20
yCentru = 20
raza = 40

# Unghiurile în raport cu axa X
unghi1 = 20 * np.pi / 180
unghi2 = 70 * np.pi / 180

# Pasul cu care desenăm arcul
pas = (unghi2 - unghi1) / 100

# Coordonatele de început ale arcului
xOld = xCentru + raza * np.cos(unghi1)
yOld = yCentru + raza * np.sin(unghi1)

# Desenăm arcul
for unghi in np.arange(unghi1 + pas, unghi2, pas):
    x = xCentru + raza * np.cos(unghi)
    y = yCentru + raza * np.sin(unghi)
    plt.plot([xOld, x], [yOld, y], linewidth=5, color='r')
    xOld = x  # Memorez ultima coordonată a ultimului punct trasat
    yOld = y  # Pentru a trasa de la el la următorul punct calculat

# Scriem (x1, y1)
plt.text(43, 35, '(x1,y1)', fontsize=12)

# Scriem (x2, y2)
plt.text(22, 55, '(x2,y2)', fontsize=12)

# Punctăm centrul cercului
plt.scatter(xCentru, yCentru, s=50, color='k')

# Scriem (xC, yC)
plt.text(xCentru - 4, yCentru + 4, '(xC,yC)', fontsize=12)

plt.show()