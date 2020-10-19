import numpy as np 
from scipy.sparse import coo_matrix
from sklearn.naive_bayes import MultinomialNB,BernoulliNB
from sklearn.metrics import accuracy_score

path='data/'
train_data_fn='train-features.txt'
train_label_fn='train-labels.txt'
test_data_fn='test-features.txt'
test_label_fn='test-labels.txt'

n_words=2500 #size for each vector


def readData(data_fn, label_fn):
	with open(path+label_fn) as f:
		content=f.readlines()

	label=[int(x.strip()) for x in content]

	with open(path+data_fn) as f:
		content=f.readlines()

	content=[x.strip() for x in content]
	dataBeforeConvertToFrequency=np.zeros((len(content),3),dtype=int)

	for i,line in enumerate(content):
		a=line.split(' ')
		dataBeforeConvertToFrequency[i:,]=np.array([int(a[0]),int(a[1]),int(a[2])])

	#-1 because index start 0
	data=coo_matrix((dataBeforeConvertToFrequency[:,2],(dataBeforeConvertToFrequency[:,0]-1,dataBeforeConvertToFrequency[:,1]-1)),
		shape=((len(label),n_words)))
	return (data,label)
	
	


if __name__=="__main__":
	(data_train,label_train)=readData(train_data_fn,train_label_fn)
	(data_test,label_test)=readData(test_data_fn,test_label_fn)

	model=MultinomialNB()
	model.fit(data_train,label_train)


	predict_for_datatest=model.predict(data_test)

	print("Train size =%d\nAccuracy Score %0.2f%%"%(data_train.shape[0],accuracy_score(predict_for_datatest,label_test)*100))


