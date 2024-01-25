#by ebi
n = int(input())
radif = [1]
for _ in range(n):
    print(" ".join ( map ( str, radif ) ) )
    radif = [ 1 ] + [ radif [ i ] + radif [ i + 1 ] for i in range( len ( radif ) - 1 ) ] + [ 1 ]


