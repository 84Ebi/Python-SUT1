#by ebi
dupcheck = set()
n = int(input())
for _ in range(n):
    input1 = input()
    if "@" in input1:
        _, domain = input1.split('@', 1)
        dupcheck.add(domain)
finalres = sorted(dupcheck)
for item in finalres:
    print(item)
