import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')

def fob(x1, x2):
    fob = np.power(x1 - 1, 2) + 2 * np.power(x2, 2)
    grad = np.array([2*(x1-1), 4*x2])
    return fob, grad


def dk(x0):
    return -fob(x0[0], x0[1])[1] / np.abs(fob(x0[0], x0[1])[0])


def alpha(dk, x0 ):
    alphax = (dk[0] - x0[0] * dk[0] - 2 * x0[1] * dk[1]) / (np.power(dk[0], 2) + 2 * np.power(dk[1], 2))
    return alphax


def gradientDescent(x0, fob):
    max_it = 100
    e = 0.01
    res = []
    for i in range(max_it):
        gk = fob(x0[0], x0[1])[0]
        d = dk(x0)
        alph = alpha(d, x0)
        x_old = float(fob(x0[0], x0[1])[0])
        res.append([x_old, x0])
        x0 = x0 + alph * d
        x_new = float(fob(x0[0], x0[1])[0])
        if np.abs(x_new - x_old) < e:
            print("Precision achieved")
            res.append([x_new, x0])
            return np.array(res)
    print("Max of iterations achieved")
    res.append([x_new, x0])
    return np.array(res)


# Fob plot
x1 = np.arange(-10, 10, 0.1)
x2 = -x1
x1, x2 = np.meshgrid(x1, x2)
z = fob(x1, x2)
fig, ax = plt.subplots(1)
ax2 = ax.contour(x1, x2, z[0], cmap=plt.get_cmap('rainbow'))
ax.clabel(ax2, inline=1, fontsize=10)
plt.show()


# Iterations plot
x0 = np.array([10, 10])
res = gradientDescent(x0, fob)

fig, ax = plt.subplots(figsize=(12, 8))
_ = ax.plot(range(len(res)), res[:, 0, ], 'ro')
plt.ylabel('FOB')
plt.xlabel('Iterations')
print(res)

# Min plot
fig, ax = plt.subplots(1)
ax2 = ax.contour(x1, x2, z[0], cmap=plt.get_cmap('rainbow'))
plt.plot(res[-1][1][0], res[-1][1][1], 'ro')
print(res[-1][1][0], res[-1][1][1])
ax.clabel(ax2, inline=1, fontsize=10)
plt.show()