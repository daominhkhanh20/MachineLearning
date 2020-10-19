from csv import reader
from math import sqrt

def loadFileCsv(filename):
    dataset=list()
    with open(filename,"r") as file:
        csv_reader=reader(file)
        for row in csv_reader:
            if not row: #skip the first row
                continue
            dataset.append(row)
    
    return dataset

def convertDataFromStringToFloat(dataset,index):
    for row in dataset:
        row[index]=float(row[index].strip())

#assign label int for flower
def convertFlowerItemToInt(dataset,lastIndexRow):
    listItemFlower=[row[lastIndexRow] for row in dataset]
    setItem=list(set(listItemFlower))

    assignItemToInt=dict()
    for i in range(len(setItem)):
        assignItemToInt[setItem[i]]=i
    
    for row in dataset:
        row[lastIndexRow]=assignItemToInt[row[lastIndexRow]]
    
    return assignItemToInt

def distance2Point(x, data):
    distance=0.0
    for i in range(len(data)):
        distance+=(x[i]-data[i])**2

    return sqrt(distance)

def getNeighbor(dataset,data,number_neighbor):
    listDistance=list()
    for row in dataset:
        listDistance.append((row,distance2Point(row,data)))
    
    neighbor=[]
    listDistance.sort(key=lambda tup:tup[1])
    for i in range(number_neighbor):
        neighbor.append(listDistance[i][0])

    return neighbor
    


def predictedClassification(dataset,data,number_neighbor):
    neighbor=getNeighbor(dataset,data,number_neighbor)
    
    output=[row[-1] for row in neighbor]
    prediction=max(set(output),key=neighbor.count)#find item with maximum frequency in list
    return prediction


if __name__ =="__main__":
    fileName="Algorithms/KNN/iris.csv"
    dataset=loadFileCsv(fileName)
    for i in range(len(dataset[0])-1):
        convertDataFromStringToFloat(dataset,i)
    
    setFlower=convertFlowerItemToInt(dataset,len(dataset[0])-1)
    
    print(setFlower)
    data=[6.4,3.2,4.5,1.5]#data for a flower need predicted
    number_neighbor=5
    prediction=predictedClassification(dataset,data,number_neighbor)

    print("Data:%s Prediction:%s"%(data,prediction))
