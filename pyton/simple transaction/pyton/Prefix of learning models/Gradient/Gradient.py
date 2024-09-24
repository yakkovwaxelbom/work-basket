import numpy as np
from typing import Callable


def find_min_f(f: Callable[[np.ndarray], float],d):
    step_size = 0.00001
    point = np.random.randint(-10, 10, size=d).astype('float')
    for i in range(50000):
        # step_size *= 1.01
        # print(i, point, foo(point), step_size, get_gradient(f, point))
        point -= step_size * get_gradient(f, point)
    return point


def get_gradient(f: Callable[[np.ndarray], float], point: np.ndarray):
    gradient = []
    for idx in range(point.size):
        gradient.append(derivative(f, point, idx))
    return np.array(gradient)


def derivative(foo, x, idx):
    h = 0.00001
    xh = x.copy()
    xh[idx] += h
    return (foo(xh) - foo(x)) / h


def f(beata_alfa: np.array):
    beata, alfa = list(beata_alfa)[0],list(beata_alfa)[1]
    x = np.array([i for i in range(-100, 110, 10)])
    y = np.array([3 * i - 5 for i in x])
    return ((-x*beata-alfa+y)**2).sum()


a = np.array([4])
# print(f(a))

# print(find_min_f(f, 2))

# beta = -5 , alpha = 3
point = np.random.randint(-10, 10, size=10).astype('float')
# print(point)
