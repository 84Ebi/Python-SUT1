#by ebi
def dtb(n): 
    return "{:032b}".format(int(n))
r = str(input())
ch = str(input())
n = int(input())
if __name__ == '__main__': 
    chap = str(dtb(int(ch)))
    rast = str(dtb(int(r)))
list=[]
dt = str(chap)+str(rast)
for i in range(n):
    m = int(input())
    if dt[-m-1]=='0':
        list.append('no')
    elif dt[-m-1]=='1':
        list.append('yes')
for a in range(len(list)):
    print(list[a])