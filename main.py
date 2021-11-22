import numpy as np
import matplotlib.pyplot as plt
import csv


def main():
    def estimate_a_b(x, y):
        n = np.size(x)
        x_mean = np.mean(x)
        y_mean = np.mean(y)
        x_squared_sumatory = sum(x ** 2)
        xy_sumatory = sum(x*y)
        x_variance = x_squared_sumatory / n - x_mean**2
        covariance = xy_sumatory / n - x_mean*y_mean
        # pendiente
        a = covariance / x_variance
        b = y_mean - a*x_mean
        return a, b, covariance

    with open('horno.csv', 'r') as file:
        content = list(csv.reader(file))
    # independent var
    y = np.array([float(data[0]) for data in content[1:]])
    # dependent var 1
    x1 = np.array([float(data[1]) for data in content[1:]])
    # dependent var 2
    x2 = np.array([float(data[2]) for data in content[1:]])
    a, b, covar = estimate_a_b(x1, y)

    X = x1
    Y = a*x1 + b
    print(f'La recta de regresión es: y = {a:.2e}x{b:+.2e}')
    print(f'La covarianza es: {covar:.2f}')

    plt.scatter(x1, y)
    plt.plot(X,Y, color='red')
    plt.show()


if __name__ == '__main__':
    main()


