from math import pi, sin
from matplotlib import pyplot
from numpy import arange, argmax
from numpy.random import normal

# find max value for f=x^2*sin(5*pi-x)^6 in [0,1]


def objective_function(x, noise=0.1):
    # normal(...) return narray or scalar
    # paramater: lod =mean  scale=standard deviation for normal distribution

    noise = normal(loc=0, scale=noise)
    return x**2 * (sin(5 * pi * x)**6.0) + noise


if __name__ == "__main__":
    # input: random value in area 0 to 1
    X = arange(0, 1, 0.01)
    y_without_noise = [objective_function(x, 0) for x in X]
    y_noise = [objective_function(x) for x in X]
    index_max = argmax(y_without_noise)
    print("Optimal : x=%0.3f y=%0.3f" %
          (X[index_max], y_without_noise[index_max]))
    # or pyplot.plot(X,y_noise,'.')
    pyplot.scatter(X, y_noise)
    pyplot.plot(X, y_without_noise)
    pyplot.show()
