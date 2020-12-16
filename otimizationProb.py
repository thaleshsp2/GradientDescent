# importar numpy e pandas
import numpy as np
#import pandas as pd
import matplotlib.pyplot as plt
#import matplotlib.cm as cm

delta = 0.5
x = np.arange(-10, 10, delta)
y = np.arange(-10, 10, delta)

X, Y = np.meshgrid(x, y)
Z = X**2 + Y**2

fig, ax = plt.subplots()
CS = ax.contour(X, Y, Z, cmap=plt.get_cmap('rainbow'))
ax.clabel(CS, inline=1, fontsize=10)
ax.set_title('f(x)')
ax.set_xlabel('x1')
ax.set_ylabel('x2')
plt.show()
