import numpy as np
import matplotlib.pyplot as plt
import csv

def estimate_a_b(x,y):
    n = np.size(x)
    x_mean = np.mean(x)
    y_mean = np.mean(y)
    y_squared_sumatory = sum(y ** 2)
    xy_sumatory = sum(x*y)
    y_variance = y_squared_sumatory / n - y_mean**2
    covariance = xy_sumatory / n - x_mean*y_mean
    # pendiente
    a = covariance / y_variance
    b = y_mean - a*x_mean
    return a, b


with open('insurance.csv', 'r') as file:
    content = list(csv.reader(file))
# independent var
age = np.array([int(data[0]) for data in content[1:]])
# dependent var
charges = np.array([float(data[6]) for data in content[1:]])

a, b = estimate_a_b(age, charges)
print(f'La recta de regresi�n es: y = {a:.2f}x{b:+.2f}')

plt.scatter(age, charges)
plt.show()


if __name__ == '__main__':
    estimate_m_n()


