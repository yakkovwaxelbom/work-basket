import numpy as np
from Gradient import find_min_f
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# MSR
"beata_alfa are a vector whose last component is alpha and the other"
" components are beta and t are a matrix each row is x_i respectively "


class MSR:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def f(self, beata_alfa):
        alpha, beta, = np.array(list(beata_alfa[:-1])), np.array(list(beata_alfa[-1:]))
        # print(beata,alfa)
        return np.sum((self.x * beta + alpha - self.y) ** 2)


# return (np.reshape((beata * self.x + alfa).sum(axis=1), (len(self.x), 1)) - self.y).sum()


"Task: make an error function for samples with m parameters"

"test"
x = np.array([i for i in range(-100, 110, 10)]).reshape(-1, 1)
y = np.array([3 * i - 5 for i in x]).reshape(-1, 1)

reg = LinearRegression().fit(x, y)
alpha = reg.intercept_
beta = reg.coef_[0]
print(alpha, beta)  # alpha = -5 beta = 3

model = MSR(x, y)
print(find_min_f(model.f, 2))  # alpha ≈ -5 beta ≈ 3


"test_1"
x_1 = np.random.normal(5, 2, 1000)
y_1 = 2 * x_1 + 3

model_1 = MSR(x_1, y_1)
alpha, beta = find_min_f(model_1.f, 2)  # alpha ≈ 3 beta ≈ 2

max_point = max(list(x_1))
min_point = min(list(x_1))
ref_line_x = [min_point, max_point]
ref_line_y = [min_point * beta + alpha, max_point * beta + alpha]
plt.plot(ref_line_x, ref_line_y, label='line regression')
plt.scatter(x_1, y_1, )
plt.show()
