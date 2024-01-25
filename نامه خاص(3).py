#by ebi
numbers = input()
targ = int(input())
numlist = numbers.split()
dict1 = dict()
findict = dict()
for index,item in enumerate(numlist):
    dict1[int(item)]=index

for i in dict1.keys():
    tmp = targ - i
    if tmp in dict1 and tmp!=i:
        sum1 = dict1[i]+dict1[tmp]
        if (tmp,i) not in findict.keys():
            findict[(i,tmp)]=sum1
finalres = sorted(findict.values())
if not findict:
    print("Not Found!")

else:
    for k in finalres:
        print(k)