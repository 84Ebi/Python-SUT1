#by ebi
def main():
    item = inp.split(' ')
    item.sort(key=lambda x: int(x[1:]))
    for i in item:
        print(i[0],end='')
inp=str(input())
main()