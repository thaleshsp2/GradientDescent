# importar numpy e pandas
import numpy as np
#import pandas as pd
import matplotlib.pyplot as plt
#import matplotlib.cm as cm

delta = 0.5
x1 = np.arange(-10, 100, delta)
x2 = np.arange(-100, 10, delta)

X1, X2 = np.meshgrid(x1, x2)
Z = (X1 -1)**2 + 2*(X2**2)

fig, ax = plt.subplots()
CS = ax.contour(X1, X2, Z, cmap=plt.get_cmap('rainbow'))
ax.clabel(CS, inline=1, fontsize=10)
ax.set_title('f(x)')
ax.set_xlabel('x1')
ax.set_ylabel('x2')
plt.show()
