import numpy as np
import matplotlib.pyplot as plt

# Setarea axelor
plt.axis([0, 100, 87, 10])
plt.axis('on')
plt.grid(False)

# Centrul și raza arcului principal
xc, yc, r = 20, 20, 40
plt.scatter(xc, yc, color='b', s=5)

# Unghiurile
phi1 = 20 * np.pi / 180
phi2 = 70 * np.pi / 180
dphi = (phi2 - phi1) / 20

for phi in np.arange(phi1, phi2, dphi):
    x = xc + r * np.cos(phi)
    y = yc + r * np.sin(phi)
    plt.scatter(x, y, s=2, color='g')

plt.plot([xc, xc + r * np.cos(phi1)], [yc, yc + r * np.sin(phi1)], color='k')
plt.plot([xc, xc + r * np.cos(phi2)], [yc, yc + r * np.sin(phi2)], color='k')

# Calculul punctelor suplimentare
x1 = xc + (r + 3) * np.cos(phi1)
x2 = xc + (r + 10) * np.cos(phi1)
y1 = yc + (r + 3) * np.sin(phi1)
y2 = yc + (r + 10) * np.sin(phi1)
plt.plot([x1, x2], [y1, y2], color='k')

x1 = xc + (r + 3) * np.cos(phi2)
x2 = xc + (r + 30) * np.cos(phi2)
y1 = yc + (r + 3) * np.sin(phi2)
y2 = yc + (r + 30) * np.sin(phi2)
plt.plot([x1, x2], [y1, y2], color='k')

# Linie orizontală și verticală
plt.plot([xc, 100], [yc, yc], 'k')
plt.plot([xc, xc], [yc, 80], 'k')

# Etichete
plt.text(71, 58, 'p2', size='small')
plt.text(66, 44, 'p', size='small')
plt.text(63, 29, 'pl', size='small')
plt.text(45, 66, 'dp', size='small')
plt.text(41, 26, 'r')
plt.text(3, 17, '(xc, yc)', size='small')

# Săgeți
plt.arrow(47, 79, -2, 1, head_length=3, head_width=2, color='k')
plt.arrow(62, 53, -2, 2, head_length=2.9, head_width=2, color='k')
plt.arrow(64, 31, -0.9, 3, head_length=2, head_width=2, color='k')
plt.arrow(52, 63, 3, -3, head_length=2, head_width=2, color='k')

plt.show()