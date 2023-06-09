import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

x = np.random.randint(10, size=(7)).reshape(-1, 1)
y = np.random.randint(10, size=(7))
plt.plot(x, y, "b.");

x_new = np.c_[np.ones((7, 1)), x]
x_new

theta = np.linalg.inv(x_new.T.dot(x_new)).dot(x_new.T).dot(y)
theta

x_test = np.random.randint(10, size=(7))
x_test

x_test_2 = np.c_[np.ones((7, 1)), x_test]
x_test_2

y_perd = x_test_2.dot(theta)
y_perd

plt.plot(x_test, y_perd, "r-")
plt.plot(x, y, "b.");

