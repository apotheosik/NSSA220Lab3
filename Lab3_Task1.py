# Chris Sequeira 1 April 2022
import sys
from math import sqrt
#receive iris_full.txt

#parse file to list of rows
def read_data(filename, L):
    with open(filename, 'r') as file:
        dataFlag=False

        #only save lines after "@DATA" appears based on dataFlag
        for line in file:
            if line.strip() == "@DATA":
                dataFlag = True
            if dataFlag:
                L.append(line.strip().split(","))
            else:
                continue
    L.pop(0)


#returns min, max, and average of selected field per 1-4 passed via 'field'
def process_numeric_fields(L, field):
    min = 100 #set to 100 bc if it was set to zero it would never change
    max = 0
    gross = 0
    avg = 0

    #Label statistics based on passed field value
    if field == 1:
        identifier = "Sepal length: "
    elif field == 2:
        identifier = "Sepal width: "
    elif field == 3:
        identifier = "Petal length: "
    elif field == 4:
        identifier = "Petal width: "

    #arrays start at zero, so we repurpose passed value as array index
    field -= 1

    for iris in L:
        value = float(iris[field])
        gross += value
        if value < min:
            min = value
        if value > max:
            max = value

    avg = gross/len(L)

    #CALCULATE STANDARD DEVIATION__________________________________________________________________________________
    squaredMeanDistanceSum = 0
    for data in L:
        #pull value at specified index
        decData = float(data[field])
        #calculate the square of the value's distance to the mean
        squaredMeanDistance = (decData - avg)**2
        #collect all values' distances to the mean
        squaredMeanDistanceSum += squaredMeanDistance

    #divide by total values and find root
    sdev = sqrt(squaredMeanDistanceSum/len(L))



    print(identifier, "min= ", round(min, 2), ", max= ", round(max, 2), ", average= ", round(avg, 2), ", standard deviation= ", round(sdev, 2))

#returns count of each type
def count_iris_types(L):
    setosa = 0
    versicolor = 0
    virginica = 0
    for i in L:
        if i[4] == "Iris-setosa":
            setosa +=1
        if i[4] == "Iris-versicolor":
            versicolor +=1
        if i[4] == "Iris-virginica":
            virginica +=1
    print("Iris Types: Iris Setosa = ", setosa, ", Iris Versicolor = ", versicolor, "Iris Virginica = ", virginica)



if __name__ == '__main__':
    L=[]
    read_data("iris_full.txt", L) #read_data(sys.argv[1], L)
    process_numeric_fields(L, 1)
    process_numeric_fields(L, 2)
    process_numeric_fields(L, 3)
    process_numeric_fields(L, 4)
    count_iris_types(L)
