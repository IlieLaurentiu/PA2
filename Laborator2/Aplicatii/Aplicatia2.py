import matplotlib.pyplot as plt
import numpy as np
import random

plt.axis([15, 90, 65, 8])
plt.axis('on')

# -- Textura 1
plt.text(19, 63, 'Textura 1', fontsize=18)

for x in np.arange(20, 40, 4):
    for y in np.arange(10, 60, 4):
        plt.scatter(x, y, s=100, color='b')

# -- Textura 2
plt.text(46, 63, 'Textura 2', fontsize=18)

for x in np.arange(45, 65, 1):
    for y in np.arange(10, 40, 1):
        plt.scatter(x, y, s=34, color='y')

for x in np.arange(45, 65, 1):
    for y in np.arange(40, 60, 1):
        plt.scatter(x, y, s=34, color='g')

for x in np.arange(50, 65, 1):
    for y in np.arange(25, 30, 1):
        plt.scatter(x, y, s=34, color='b')

plt.scatter(55, 30, s=400, color='r')

# -- Textura 3
plt.text(70, 63, 'Textura 3', fontsize=18)

for x in np.arange(70, 90, 2):
    for y in np.arange(10, 60, 2):
        rr = random.randrange(0, 100, 1) / 100
        rg = random.randrange(0, 100, 1) / 100
        rb = random.randrange(0, 100, 1) / 100
        plt.scatter(x, y, s=150, color=(rr, rg, rb))

plt.show()