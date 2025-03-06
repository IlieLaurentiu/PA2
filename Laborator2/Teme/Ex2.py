import numpy as np
import matplotlib.pyplot as plt

plt.axis([-65, 73, 50, -42])
plt.grid(True)

# Cercul verde
xc, yc, r = 0, 0, 40
p1, p2 = 0 * np.pi / 180, 360 * np.pi / 180
dp = (p2 - p1) / 100

xlast = xc + r * np.cos(p1)
ylast = yc + r * np.sin(p1)

for p in np.arange(p1, p2 + dp, dp):
    x = xc + r * np.cos(p)
    y = yc + r * np.sin(p)
    if 90 * np.pi / 180 < p < 270 * np.pi / 180:
        plt.plot([xlast, x], [ylast, y], color='g', linestyle=':')
    else:
        plt.plot([xlast, x], [ylast, y], color='g')
    xlast = x
    ylast = y

plt.scatter(xc, yc, s=15, color='g')

# Cercul roșu
xc, yc, r = -20, -20, 10
p1, p2 = 0 * np.pi / 180, 360 * np.pi / 180
dp = (p2 - p1) / 100

xlast = xc + r * np.cos(p1)
ylast = yc + r * np.sin(p1)

for p in np.arange(p1, p2 + dp, dp):
    x = xc + r * np.cos(p)
    y = yc + r * np.sin(p)
    plt.plot([xlast, x], [ylast, y], linewidth=4, color='r')
    xlast = x
    ylast = y

plt.scatter(xc, yc, s=15, color='r')

# Cercul violet
xc, yc, r = 20, 20, 50
p1, p2 = 0 * np.pi / 180, 360 * np.pi / 180
dp = (p2 - p1) / 100

xlast = xc + r * np.cos(p1)
ylast = yc + r * np.sin(p1)

for p in np.arange(p1, p2 + dp, dp):
    x = xc + r * np.cos(p)
    y = yc + r * np.sin(p)
    plt.plot([xlast, x], [ylast, y], linewidth=2, color=(0.8, 0, 0.8))
    xlast = x
    ylast = y

# Discul albastru
xc, yc, r1, r2, dr = -53, -30, 0, 10, 1
p1, p2 = 0 * np.pi / 180, 360 * np.pi / 180
dp = (p2 - p1) / 100

for r in np.arange(r1, r2, dr):
    xlast = xc + r * np.cos(p1)
    ylast = yc + r * np.sin(p1)
    for p in np.arange(p1, p2 + dp, dp):
        x = xc + r * np.cos(p)
        y = yc + r * np.sin(p)
        plt.plot([xlast, x], [ylast, y], linewidth=2, color=(0, 0, 0.8))
        xlast = x
        ylast = y

plt.show()