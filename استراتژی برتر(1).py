def check_adad_aval(adad):
    if adad < 2:
        return False
    for i in range(2, int(adad**0.5) + 1):
        if adad % i == 0:
            return False
    return True

a, b = map(int, input().split())

tedad_aval = 0
for adad in range(min(a, b), max(a, b) + 1):
    if check_adad_aval(adad):
        tedad_aval += 1

if a <= b:
    print(f'main order - amount: {tedad_aval}')
else:
    print(f'reverse order - amount: {tedad_aval}')
