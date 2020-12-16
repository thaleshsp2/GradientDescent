# This a implementation of Gradient Descent algorith applied to minimize FOBs.

import numpy as np
import matplotlib.pyplot as plt
np.warnings.filterwarnings('ignore', category=np.VisibleDeprecationWarning)


def fob(x1, x2):
    return np.power(x1 - 1, 2) + 2 * np.power(x2, 2)


def gradF(x1, x2):
    return np.array([2*(x1-1), 4*x2])


def plot(res):
    x1 = np.arange(-10, 10, 0.1)
    x2 = -x1
    x1, x2 = np.meshgrid(x1, x2)
    z = fob(x1, x2)
    fig, ax = plt.subplots(1)
    ax2 = ax.contour(x1, x2, z, cmap=plt.get_cmap('rainbow'))
    ax.clabel(ax2, inline=1, fontsize=10)
    plt.plot(res[-1][0][0], res[-1][0][1], marker='o')
    plt.show()


# def plotPoint(result):
#     plt.plot(result[-1][0], result[-1][], marker='o')
#     plt.plot()


def gradientDescent(x0, fob, grad):
    precision = 0.01
    learning_rate = 0.0001
    max_iter = 1000
    x_new = x0
    res = []
    for i in range(max_iter):
        x_old = x_new
        x_new = x_old - learning_rate * gradF(x_old[0], x_old[1])
        f_x_new = float(fob(x_new[0], x_new[1]))
        f_x_old = float(fob(x_old[0], x_old[1]))
        res.append([x_new, f_x_new])
        plot(res)
        if abs(f_x_new - f_x_old) < precision:
            print("Precision achieved:")
            return np.array(res)
    print("Max of iterations achieved")
    return np.array(res)

x0 = np.array([10, 10])
res = gradientDescent(x0, fob, gradF)


