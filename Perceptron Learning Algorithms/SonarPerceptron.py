#need imporve accuracy score(low)

from random import randrange,seed
from csv import reader
from sklearn.metrics import accuracy_score
import numpy as np
def read_data(file_name):
	dataset=list()
	with open(file_name,'r') as file:
		csv_reader=reader(file)
		for row in csv_reader:
			if not row:
				continue
			dataset.append(row)
	return dataset

def convert_column_into_float(dataset,index_column):
	for row in dataset:
		row[index_column]=float(row[index_column].strip())

def convert_name_to_int(dataset):
	list_name=[row[-1] for row in dataset]
	unique=set(list_name)
	lookup=dict()

	for i,value in enumerate(unique):
		lookup[value]=i

	for row in dataset:
		row[-1]=lookup[row[-1]]

def split_data(n_fold,dataset):
	folds=list()
	fold_size=int(len(dataset)/n_fold)

	for i in range(n_fold):
		new_fold=list()
		while len(new_fold)<fold_size:
			index=randrange(len(dataset))
			new_fold.append(dataset.pop(index))
		folds.append(new_fold)

	return folds

def predict(w,x):
	num=w[0]
	for i in range(len(x)):
		num+=w[i+1]*x[i]
	return 1.0 if num>=0 else 0.0

def perceptron_alogrithms(train_set,learning_rate,n_epoch):
	data_train=list()
	for fold in train_set:
		data_train=data_train+fold

	w_init=[0.0 for i in range(len(data_train[0])+1)]
	weight=w_init
	for epoch in range(n_epoch):
		for data_point in data_train:
			pre=predict(weight,data_point)
			error=pre-data_point[-1]
			weight[0]+=learning_rate*error
			for i in range(len(data_point)):
				weight[i+1]+=learning_rate*error*data_point[i]

	return weight




def scores(dataset,n_fold,learning_rate,n_epoch):
	accuracy=list()
	#split data into 3 fold
	folds=split_data(n_fold,dataset)
	for fold in folds:
		train_set=list(folds)
		#the tranning data
		train_set.remove(fold)
		#the testing data
		test_set=fold
		w=perceptron_alogrithms(train_set,learning_rate,n_epoch)
		predict_for_test_set=[predict(w,data_point) for data_point in test_set]
		output_expect=[data_point[-1] for data_point in test_set]

		true_predict=np.where(np.equal(predict_for_test_set,output_expect)== True)[0]
		print(true_predict.shape[0])

		accuracy.append(accuracy_score(predict_for_test_set,output_expect))

	return accuracy


if __name__=="__main__":
	seed(1)#determine: it can generate the same random value in mutiple executions
	file_name="/home/daominhkhanh/Desktop/MachineLearningBasic/Perceptron Learning Algorithms/sonar_csv.csv"
	dataset=read_data(file_name)#remove row 1(attribute 1,2,3,...)
	dataset.pop(0)
	for i in range(len(dataset[0])-1):
		convert_column_into_float(dataset,i)
	convert_name_to_int(dataset)
	#separate data into 3 fold, 1 fold for test data, the other for tranning data
	n_fold=3
	learning_rate=0.6
	#the number of times run through the tranning data while updating the weight
	n_epoch=1000
	accuracy_list_for_fold=scores(dataset,n_fold,learning_rate,n_epoch)
	print("List scores:",accuracy_list_for_fold)

	print("Means scores: %0.3f%%"%(sum(accuracy_list_for_fold)/len(accuracy_list_for_fold)))

