import numpy as np
from math import log
from scipy import sparse
from random import seed
import matplotlib.pyplot as plt


def softmax(z):
    exponential_z = np.exp(z)
    return exponential_z / exponential_z.sum(axis=0)


def convert_matrix_y(y):
    """
    Convert 1d label to a matrix label. In each of column in this matrix coresponding 1 element into y
    The element i-th in column j-th =1 if y[j]=i, else =0
    """
    """
	*Way 1:
	y_temp=np.zeros(n*c).reshape(c,n)
	for i in range(n):
		y_temp[Y[i]][i]=1
	return y_temp
	"""

    # Way 2:
    # expain:
    """
	 Example y=[0,2,1,0]
	 The new array is constructed from three array
	  + data
	  +i[:]: The index row in the matrix entries
	  +j[:]: The index column in the matrix entries
	   data[i[k],j[k]]=y[k]: k belong to range(len(y))


	"""
    Y = sparse.coo_matrix(
        (np.ones_like(y), (y, np.arange(len(y)))), shape=(c, len(y))).toarray()
    return Y


def softmax_loss(X, y, w, lamda=0.05):
    loss_value = 0.0
    n, c = X.shape[1], y.shape[0]
    for i in range(n):
        for j in range(c):
            xi = X[:, i].reshape(d, 1)
            weight = [np.exp(w[:, k].reshape(1, d).dot(xi)) for k in range(c)]
            ai = weight[j] / sum(weight)
            loss_value += y[j, i] * log(ai)

    # weight_decay=0.5*lamda*np.linalg.norm(w)#overfitting
    return -1 / n * (loss_value)


def softmax_regression(X, w_init, Y, eta, max_count_iter=1000, stop_condition=1e-5):
    w = [w_init]
    d = w_init.shape[0]
    c = w_init.shape[1]
    iteration = 0
    circle_check = 20
    loss_hiss = [softmax_loss(X, Y, w[-1])]

    while iteration < max_count_iter:
        mix_id = np.random.permutation(n)
        for i in mix_id:
            xi = X[:, i].reshape(d, 1)
            yi = Y[:, i].reshape(c, 1)
            ai = softmax(np.dot(w[-1].T, xi))
            # stochastic gradient desent
            w_new = w[-1] - eta * xi.dot((ai - yi).T)
            iteration += 1
            # check stop condition
            if iteration % circle_check == 0:
                if np.linalg.norm(w_new - w[-circle_check]) < stop_condition:
                    return w
            w.append(w_new)
            loss_hiss.append(softmax_loss(X, Y, w[-1]))

    return (w, loss_hiss)


def softmax_predict(x, w):
    # w is n-array with shape (d,c)
    # x is n-array with shape (d,n)
    probability = softmax(w.T.dot(x))
    # return array with shape (1,n), each element in array is value index
    # which has max value in each column at the probability matrix
    return np.argmax(probability, axis=0)


if __name__ == "__main__":

    n = 2  # number of trainning sample
    d = 2  # data demention
    c = 3  # number of classes
    seed(1)
    # initial data for x
    # each column is 1 data point
    X = np.random.rand(d, n)
    # initial the class for each data point in rang(C)
    Y = np.random.randint(0, c, (n,))
    w_init = np.random.rand(d, c)
    # in each column, index i in column j-th =1 if data point j-th belong to class i
    # Example x0 belong to class 1, thus Y[1][0]=1
    Y = convert_matrix_y(Y)
    eta = 0.05
    # list update history the weight matrix
    (w, loss_hiss) = softmax_regression(X, w_init, Y, eta)
    iteration = np.arange(1, len(loss_hiss) + 1, 1)
    plt.plot(iteration, loss_hiss, 'r', '-')
    plt.xlabel("Iterations")
    plt.ylabel("Loss value")
    plt.savefig("Visualization.png")
    plt.show()
    seed(2)
    X_test = np.random.rand(d, n)
    pre = softmax_predict(X_test, w[-1])
    print(pre)
