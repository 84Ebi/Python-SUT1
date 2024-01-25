import numpy as np
file = open("C:\\Users\ebi\Downloads\in\input10.txt", "r")
list1=list()
list2=list()
a=(file.read()).split('\n')
a.pop(-1)
for i in a:
    list2.append(i.split(" "))
n = list2[0][0]
m = int(list2[0][1])
list2.pop(0)

numbers = [item for sublist in list2 for item in sublist]
for i in range(len(numbers)):
    numbers[i] = int(numbers[i])

m = int(m)
n = int(n)

matrix = np.array(numbers).reshape((n, m, m))

maxdet = -1000
maxmatrix = None
for i in range(n):
    for j in range(i+1, n):
        tmpdet = np.linalg.det(np.dot(matrix[i], matrix[j]))

        if tmpdet > maxdet:
            maxdet = tmpdet
            maxmatrix = (matrix[i], matrix[j])
for i in range(n):
    for j in range(i+1, n):
        tmpdet = np.linalg.det(np.dot(matrix[j], matrix[i]))

        if tmpdet > maxdet:
            maxdet = tmpdet
            maxmatrix = (matrix[j], matrix[i])

if np.linalg.det(maxmatrix[0]) >= np.linalg.det(maxmatrix[1]):

    finalres = np.linalg.inv(np.dot(maxmatrix[0],maxmatrix[1]))
else:
    finalres = np.linalg.inv(np.dot(maxmatrix[1],maxmatrix[0]))
finalres = finalres.tolist()

for i in finalres:
    for j in i:
        print(round(j,3),end=" ")
    print('\n')