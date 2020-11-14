"""
0 10
1 9
2 8
3 7
4 6 
5 5 
6 4
7 3
8 2
9 1
"""

aux1 = -1
aux2 = 11
for i in range(0, 10):
    aux1 += 1
    aux2 -= 1
    print(aux1, aux2)

print()
#ou

for p, r in  enumerate(range(10, 1, -1)):
    print(p, r)