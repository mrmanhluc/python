# coding: utf-8
# phuong trinh ham bac 2. y = ax^2 + bx + c

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

a = 2
b = -2
m = 100

X = np.random.randn(m) * 10
Y = a*X**2 + b*X + np.random.randn(m) * 100

plt.plot(X, Y, 'ro')


def predict(theta1, theta2, theta3, x):
    return theta1*x**2 + theta2*x + theta3


def cost(x, y, theta1, theta2, theta3):
    y_hat = predict(theta1, theta2, theta3, x)
    return np.sum((y_hat - y)**2)/(2*m)


a, b, c = [3, 4, 5]
learning_rate = 0.00004

cost_arr = []

for i in np.arange(200000):
    predict_lear = predict(a, b, c, X)
    a = a - learning_rate * (np.sum((predict_lear - Y) * X ** 2)) / m
    b = b - learning_rate * (np.sum((predict_lear - Y) * X)) / m
    c = c - learning_rate * (np.sum((predict_lear - Y))) / m
    cost_arr.append(cost(X, Y, a, b, c))

plt.plot(cost_arr)

x0 = np.linspace(-30, 30, 20)
y0 = predict(a, b, c, x0)
plt.plot(x0, y0)

plt.plot(X, Y, 'rx')

XX = X.reshape(m, 1)
poly = PolynomialFeatures(degree=2)
XX = poly.fit_transform(XX)
model = LinearRegression()
model.fit(XX, Y)

temp = model.predict(XX)

c, b, a = model.coef_

x0 = np.linspace(-30, 30, 20)
y0 = predict(a, b, c, x0)

plt.plot(x0, y0)
plt.plot(X, Y, 'ro')