# This a implementation of Gradient Descent algorith applied to minimize FOBs.

import numpy as np
import matplotlib.pyplot as plt


# FOB
def f_x(x):
    return np.power(x + 2, 2) - 16 * np.exp(-np.power((x - 2), 2))


def main_plot():
    x = np.arange(-8, 8, 0.001) # Interval of x [-8,8]
    y = map(lambda u: f_x(u), x)
    plt.plot(x, list(y))

#main_plot()
#plt.show()


def grad_f_x(x):
    return (2 * x - 4) - 16 * (-2 * x + 4) * np.exp(-np.power(x - 2, 2))


def gradient_descent(x0, func, grad): #x0 = ponto inicial
    # precisão da solução
    precision = 0.001
    # Learning rate: muito pequeno pode demorar muito a convergir; muito grande pode fazer um 'overshoot' ao mínimo
    learning_rate = 0.0001
    # Temos de dar um limite ao número de iteracções
    max_iter = 10000
    x_new = x0
    res = []
    for i in range(max_iter):
        x_old = x_new
        # Vamos usar B = 1
        x_new = x_old - learning_rate * grad(x_old)
        f_x_new = func(x_new)
        f_x_old = func(x_old)
        res.append([x_new, f_x_new])
        print(f_x_new - f_x_old)
        if(abs (f_x_new - f_x_old) < precision):
            print("Precisão %f alcançada:" % (f_x_new - f_x_old))
            return np.array(res)
    print("Iteracção máxima alcançada")
    return np.array(res)

# Vamos então tentar encontrar o mínimo da função começando com um valor inicial de x0 = -8


x0 = 8
res = gradient_descent(x0, f_x, grad_f_x)
plt.plot(res[:, 0], res[:, 1], '+')
main_plot()
plt.show()