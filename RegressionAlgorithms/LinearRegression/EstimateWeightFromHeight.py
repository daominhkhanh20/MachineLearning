from __future__ import print_function
import matplotlib.pyplot as plt
import numpy as np

# X.T is transposed matrix
X = np.array(
    [[147, 150, 153, 158, 163, 165, 168, 170, 173, 175, 178, 180, 183]]).T
# height (cm), each row is a data point
# weight for each person
y = np.array([49, 50, 51, 54, 58, 59, 60, 62, 63, 64, 66, 67, 68])

# weight=w_1*height+w_0
# so we need fine w_0 and w_1

# X.shape[0]= size(X[0]), currently=13
# Create one array with number row is 13
one = np.ones((X.shape[0], 1))
Xbar = np.concatenate((one, X), axis=1)
print(Xbar)
A = np.dot(Xbar.T, Xbar)  # multiplication 2 matrix
b = np.dot(Xbar.T, y)
w = np.dot(np.linalg.pinv(A), b)  # b=Aw ==>w=A^-1*b
w_0, w_1 = (float)(w[0]), (float)(w[1])
print("Input height=169 cm ==> weight=", w_1 * 169 + w_0)

x = X.T.tolist()[0]
plt.plot(x, y, '.')  # show all point (x,y) in graph

x_arr = np.array(x)
plt.plot(x, w_1 * x_arr + w_0, '-')  # show straight line
plt.show()
