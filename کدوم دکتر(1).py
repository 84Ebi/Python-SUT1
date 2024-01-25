def dtb(n): 
    return "{0:b}".format(int(n))
a=input()
b=input()
if __name__ == '__main__': 
    sa=str(dtb(a))
    sb=str(dtb(b))


sa= (str(10**(100-len(sa)))+sa)
enum = 0
sb =(str(10**(100-len(sb)))+sb)

for i in range(101):
    if sa[-i] != sb[-i]:
        enum +=1
print(enum)