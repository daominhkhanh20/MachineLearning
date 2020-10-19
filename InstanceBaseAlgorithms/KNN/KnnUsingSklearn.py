import numpy as np
#pick up dataset iris
from sklearn import neighbors, datasets 
# because the input data is string, so we need convert string to datatype
# depend on the data such that float, int, double
from sklearn.model_selection import train_test_split 
# for evaluating result (performance predicted)
from sklearn.metrics import accuracy_score 



irisDataset=datasets.load_iris()
#pick up list information for iris, each element has 4 attribute 
#sepal length, sepal width, petal length, petal width
iris_x=irisDataset.data
# name flower
iris_y=irisDataset.target

print("Label:",np.unique(iris_y))#assign label to int

np.random.seed(7)
# x_: data  y_ target
x_train, x_test, y_train, y_test = train_test_split(iris_x, iris_y, test_size=130)

#1NN: performance is quite low 92.31%
model=neighbors.KNeighborsClassifier(n_neighbors=1,p=2)
model.fit(x_train,y_train)  #training model
y_pred=model.predict(x_test) # list y predicted after training x_test
print("accuracy of 1NN: %.2f "%(100*accuracy_score(y_test,y_pred)))


#7NN: 93.85%
model=neighbors.KNeighborsClassifier(n_neighbors=7,p=2)
model.fit(x_train,y_train)  #training model
y_pred=model.predict(x_test) # list y predicted after training x_test
print("accuracy of 7NN: %.2f "%(100*accuracy_score(y_test,y_pred)))
