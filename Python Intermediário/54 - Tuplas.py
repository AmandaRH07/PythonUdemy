# Tuplas não podem ser editadas

t1 = ("a", "João",1,2,3,4,5)
t2 = 6,7,8,9,10
t3 = t1 + t2

print(t3)

for v in t1:
    print(v)

print(t1[2:])

n1 , n2, n3, *_ , n10= t3

print(n2)
print(n10)

t4 = (1,2,"A",4,5)*3
print(t4)

t5 = (1,2,3,4,5)
t5 = list(t5) # converte para lista
t5[1] = 3000 # altera o valor
print(t5)

t5 = tuple(t5) # volta para tupla