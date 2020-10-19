import numpy as np 
from sklearn.naive_bayes import MultinomialNB,BernoulliNB


#train data
d1=[2,1,1,0,0,0,0,0,0]
d2=[1,1,0,1,1,0,0,0,0]
d3=[0,1,0,0,1,1,0,0,0]
d4=[0,1,0,0,0,0,1,1,1]
train_data=np.array([d1,d2,d3,d4])
label_for_train_data=np.array(['B','B','B','N'])

#test data
d5=np.array([[2,0,0,1,0,0,0,1,0]])
d6=np.array([[0,1,0,0,0,0,0,1,1]])

#model=MultinomialNB()# using naive bayes
#or using bernoulli
model =BernoulliNB()
model.fit(train_data,label_for_train_data)

#predicted for test data

print(model.predict(d5)) #return string array
print("Predicting class for d5:", str(model.predict(d5)[0]))
print("Probabilitiy of d6 in each of class :",model.predict_proba(d6))
