import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial.distance import cdist


def KMeansDisplay(X, lable, centroid):
    k = np.amax(lable)+1  # np.amax return the max value in array
    X0 = X[lable == 0, :]  # return all data point has lable =0
    X1 = X[lable == 1, :]
    X2 = X[lable == 2, :]
    #X0[:,:] pick up data from column 0, similar (x,y),we pick up x
    plt.plot(X0[:, 0], X0[:, 1], 'b^', markersize=4, alpha=.8)
    plt.plot(X1[:, 0], X1[:, 1], 'go', markersize=4, alpha=.8)
    plt.plot(X2[:, 0], X2[:, 1], 'rs', markersize=4, alpha=.8)

    cen1, cen2, cen3 = centroid
    plt.plot(centroid[:, 0], centroid[:, 1], 'y^',markersize=15)

    plt.axis('equal')
    plt.show()
    plt.savefig("Visualization.png")

def kmeans_init_centers(X, k):
    # randomly pick k rows of X as initial centers
    #Note
    #np.random.choice(X.shape[0],k,replace=False) pick up 1 list has k values, each k is a index we need find
    return X[np.random.choice(X.shape[0], k, replace=False)]


def kmeans_assign_labels(X, centers):
    #return array[N][3], each a[i][j] is distance from X[i] to center[j]
    D = cdist(X, centers)

    #np.argmin(D,axis=1) retrun list has values , each element is values statisfied
    #return j if a[i][j] is minimum value in row i)
    return np.argmin(D, axis=1)


def update_centers(X, label, k):
    #example x[100][10]
    #so x.shape=(100,10)
    #so x.shape[1]=10
    new_centers = np.zeros((k, X.shape[1]))
    for i in range(k):
        xi = X[lable == i, :]
        #caculate average for center[i]
        #axis=0 means calculate for each column
        #axis=1 means aclculate for each row
        new_centers[i, :] = np.mean(xi, axis=0)

    return new_centers


#check whether center is similar new_center
def hasConverged(new_center, center):
    #return (new_center==center).all()
    return set(tuple(a) for a in new_center) == set(tuple(b) for b in center)


def KMeansClusteringAlgorithms(X, k):
    centers = [kmeans_init_centers(X, k)]
    label = []
    countWhile = 0
    while True:
        label.append(kmeans_assign_labels(X, centers[-1]))
        new_centers = update_centers(X, lable[-1], k)
        if hasConverged(new_centers, centers[-1]):
            break
        centers.append(new_centers)
        countWhile += 1

    return (centers, label, countWhile)


if __name__ == "__main__":
    means = [[2, 2], [8, 3], [3, 6]]
    K = 3
    covariance_matrix = [[1, 0], [0, 1]]
    N = 50
    #random value for dataset
    #normal distribution with expectation value is means[i][0] and deviation is means[i][1]
    X0 = np.random.multivariate_normal(means[0], covariance_matrix, N)
    X1 = np.random.multivariate_normal(means[1], covariance_matrix, N)
    X2 = np.random.multivariate_normal(means[2], covariance_matrix, N)
    #concatenate 2 array along the vertical axis
    X = np.concatenate((X0, X1, X2), axis=0)
    lable = np.asarray([0]*N+[1]*N+[2]*N).T

    (centers, label, countWhile) = KMeansClusteringAlgorithms(X, K)
    print("Centroid for dataset with K cluter")
    print(centers[-1])
    KMeansDisplay(X, lable, centers[-1])
