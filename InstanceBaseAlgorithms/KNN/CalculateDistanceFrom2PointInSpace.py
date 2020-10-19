import numpy as np
from time import time
import math


def dis_pp(z, x):
    d = z-x.reshape(z.shape)
    return np.sum(d*d)

# in fact X=[x1,x2,x3,x4,x5,....,xn]^T
# this function calculate distance from z to each row in x


def dis_ps_navie(z, x):
    # x.shape[0] retrun number of element in row[0]
    n = x.shape[0]
    # create a array has 1 row and n column
    res = np.zeros((1, n))
    for i in range(n):
        res[0][i] = dis_pp(z, x[i])

    return res


if __name__ == "__main__":
    d, N = 5, 10
    X = np.random.randn(N, d)  # create array[N][d] N row d column
    print(X)
    z = np.random.randn(d)  # 1 vector
    t1 = time()
    D = dis_ps_navie(z, X)

    timeExcute = time()-t1  # time excute function
    print("time excute function", timeExcute)
    distance = math.sqrt(sum(D[0]))
    print(distance)
