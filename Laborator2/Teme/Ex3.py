import matplotlib.pyplot as plt
import numpy as np

def unghi(xCentru, yCentru, unghil, unghi2, raza=20):
    unghil = unghil * np.pi / 180
    unghi2 = unghi2 * np.pi / 180
    pas = (unghi2 - unghil) / 100

    xOld = xCentru + raza * np.cos(unghil)  # coordonatele de început ale arcului
    yOld = yCentru + raza * np.sin(unghil)

    for unghi in np.arange(unghil + pas, unghi2, pas):
        x = xCentru + raza * np.cos(unghi)
        y = yCentru + raza * np.sin(unghi)
        plt.plot([xOld, x], [yOld, y], linewidth=3, color='k')
        xOld = x  # memorez ultima coordonată
        yOld = y

plt.axis([0, 150, 100, 0])
plt.axis('on')
plt.grid(linestyle=':')

# Trasare laturi triunghi
plt.plot([20, 80], [80, 20], linewidth=3, color='k')  # latura AB
plt.plot([80, 120], [20, 80], linewidth=3, color='k')  # latura AC
plt.plot([20, 120], [80, 80], linewidth=3, color='k')  # latura BC

# Vârfurile triunghiului
plt.text(78, 18, 'A', color='k', fontsize=22)
plt.text(13, 80, 'B', color='k', fontsize=22)
plt.text(120, 80, 'C', color='k', fontsize=22)

# Arcele unghiurilor
# Din A (80 de grade)
xCentru, yCentru = 80, 20
unghil, unghi2 = 56, 136
unghi(xCentru, yCentru, unghil, unghi2)

# Din B (44 de grade)
xCentru, yCentru = 20, 80
unghil, unghi2 = -44, 0
unghi(xCentru, yCentru, unghil, unghi2)

# Din C (56 de grade)
xCentru, yCentru = 120, 80
unghil, unghi2 = -180, -124
unghi(xCentru, yCentru, unghil, unghi2)

# Valorile unghiurilor
plt.text(74, 36, '80°', color='k', fontsize=16, fontstyle='italic')  # unghiul A
plt.text(26, 78, '44°', color='k', fontsize=16, fontstyle='italic')  # unghiul B
plt.text(103, 78, '56°', color='k', fontsize=16, fontstyle='italic')  # unghiul C

# Cota lungimii laturii BC
plt.arrow(23, 90, -0.5, 0, head_length=2, head_width=1.5, color='k')  # vârf săgeată
# Cota stânga
plt.plot([58, 23], [90, 90], linewidth=0.5, color='k')  # linie orizontală cota stânga
plt.arrow(117.5, 90, 0.5, 0, head_length=2, head_width=1.5, color='k')  # vârf săgeată
# Cota dreapta
plt.plot([82, 118], [90, 90], linewidth=0.5, color='k')  # linie orizontală cota dreapta
plt.plot([20, 20], [80, 95], linewidth=1, color='k')  # cota verticală stânga
plt.plot([120, 120], [80, 95], linewidth=1, color='k')  # cota verticală dreapta

plt.text(59, 91.5, '100 cm', color='k', fontsize=14)  # 100 cm

plt.show()



