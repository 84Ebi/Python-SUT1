def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcd(a, b):
    return abs(a * b) // gcd(a, b)

mode = input()
if mode == "sum":
    totalsum = 0
    while True:
        input1 = input()
        if input1 == 'end':
            break
        totalsum += int(input1)
    print(totalsum)

elif mode == 'average':
    totalsum = 0
    tmp = 0
    while True:
        input1 = input()
        if input1 == 'end':
            break
        totalsum += int(input1)
        tmp += 1
    if tmp > 0:
        average = totalsum / tmp
        print(round(average, 2))

elif mode == 'min':
    minimum = float('inf')
    while True:
        input_str = input()
        if input_str == 'end':
            break
        input1 = int(input_str)
        minimum = min(minimum, input1)
    print(minimum)


elif mode == 'max':
    listmax=[]
    while True:
        input1 = input()
        if str(input1)=='end':
            break 
        listmax.append(int(input1))
    print(max(listmax))


elif mode =='lcd':
    list1 = []
    while True:
        input1 = input()
        if input1 == 'end':
            break
        list1.append(int(input1))
    while len(list1)!= 1:
        tmp = lcd(list1[0],list1[1])
        a = list1[0]
        b = list1[1]
        list1.remove(a)
        list1.remove(b)
        list1.append(tmp)
    print(list1[0])


elif mode =='gcd':
    list1 = []
    while True:
        input1 = input()

        if input1 == 'end':
            break
        
        list1.append(int(input1))
    while len(list1)!= 1:
        tmp = gcd(list1[0],list1[1])
        a = list1[0]
        b = list1[1]
        list1.remove(a)
        list1.remove(b)
        list1.append(tmp)
    print(list1[0])
else:
    print('Invalid command')