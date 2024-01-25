#by ebi
def binbasen(num, base):
    result = ""
    while num > 0:
        tmpbin = num % base
        result = str(tmpbin) + result
        num //= base
    return result

list1=[]
checkbase=0
while True:
    tmp=0
    num, base = map(int, input().split())

    if int(num)+int(base)==-2:
        if checkbase>0:
            print('invalid base!')
            exit()
        elif checkbase==0:    
            break
    if base <2 or base>=10:
        checkbase+=1 
    for i in range(1,num+1):
        if num%i==0:
            tmp+=(num//i)
        
    list1.append(binbasen(tmp, base))

finalans = 0
for i in range(len(list1)):
    finalans += int(list1[i])
print(finalans)