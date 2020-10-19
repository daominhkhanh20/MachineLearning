from csv import reader
from math import sqrt,pi,pow,exp

#read data from file csv
def reader_data(filename):
	dataset=list()
	with open(filename,'r') as file:
		csv_reader=reader(file)

		for row in csv_reader:
			if not row:
				continue
			dataset.append(row)

	return dataset


def convert_data_to_float(dataset,index):
	for row in dataset:
		row[index]=float(row[index].strip())

#assign name flower to integer
def convert_name_flower_to_int(dataset,index):
	name_flower=[row[index] for row in dataset]
	unique_value=set(name_flower)

	temp=dict()
	for value,name_flower in enumerate(unique_value):
		temp[name_flower]=value# value is integer
		print("%s==>%d"%(name_flower,value))

	for row in dataset:
		row[index]=temp[row[index]]

#split dataset into cluster value, return dictionary
def separated_data_for_each_class(dataset):
	summaries=dict()
	for i in range(len(dataset)):
		vector=dataset[i]
		value=vector[-1]
		if value not in summaries:
			summaries[value]=list()

		summaries[value].append(vector)

	return summaries

#calculate expectation for normal distribution
def mean(column):
	return sum(column)/len(column)

#calculate the value for variance by using unbiased estimate of variance
def variance(column):
	expectation=mean(column)
	temp=sum((x-expectation)**2 for x in column)/(len(column)-1)
	return sqrt(temp)

def calculate_expectation_variance_for_each_class(rows):
	temp=[(mean(column),variance(column),len(column)) for column in zip(*rows)] # zip(*row) select each column
	del(temp[-1])#because the end column is name flower
	return temp

 
def summaries_by_class(dataset):
	seperated=separated_data_for_each_class(dataset)
	summaries=dict()

	for value,rows in seperated.items():
		#return list (expectation, variance) for each column in each class for each name flower
		summaries[value]=calculate_expectation_variance_for_each_class(rows)

	return summaries


def normal_distribution(expectation,variance,x):
	return exp(-(pow(x-expectation,2)/(2*variance**2)))/(sqrt(2*pi)*variance)


#calculate probabilites used bayes formula
def calculate_probabilities(model,data):
	total_element_in_dataset=sum(model[value][0][2] for value in model)
	probabilities=dict()

	#bayes probabilities: P(XC)=P(C)*P(X|C)
	for value,rows in model.items():
		probabilities[value]=model[value][0][2]/float(total_element_in_dataset)# P(C)

		for i in range(len(rows)):
			mean,var,_=rows[i]
			probabilities[value]*=normal_distribution(mean,var,data[i]) # P(Xi|C)

	return probabilities

#predict for a given data, return label for data
def predict(model,data_predict):
	probabilities=calculate_probabilities(model,data)
	label,pro=None,-1
	for value,pro_for_each_class in probabilities.items():
		if label is None or pro_for_each_class>pro:
			label=value
			pro=pro_for_each_class

	return label

if __name__=="__main__":
	fileName="/home/daominhkhanh/Desktop/MachineLearningBasic/NaiveBayes/IrisFlower/iris.csv"
	dataset=reader_data(fileName)
	for index in range(len(dataset[0])-1):
		convert_data_to_float(dataset,index)

	convert_name_flower_to_int(dataset,len(dataset[0])-1)

	model=summaries_by_class(dataset)
	data=[6.2,2.3,4.6,1]

	label=predict(model,data)
	print("For ",data," Preidct:",label)