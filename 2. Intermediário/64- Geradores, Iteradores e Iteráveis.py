# Geradores, Iteradores e Iteráveis
# Iterado
# Iterador
# Gerador: usado quando gasta muita memória

import sys
import time

lista = [0,1,2,3,4,5]
#lista = 12345

#== Conferir se é iteravel
print(hasattr(lista, "__iter__"))

#== Conferir se tem mais itens, se tem é iterador
print(hasattr(lista, "__next__"))

lista = iter(lista)

print(next(lista))
print(next(lista))
print(next(lista))
print(next(lista))
print(next(lista))
print(next(lista))

print(hasattr(lista, "__next__"))


#== Tranforma a lista em iterador
for v in lista:
    print(v)

print("-------------------")

#== Geradores

lista2 = list(range(100))

print(sys.getsizeof(lista2))

print("-------------------")

def gera():
    #r = []
    for n in range(10):
        #r.append(n)
        yield n
        time.sleep(0.1)
    #return r

g = gera()

print(hasattr(g, '__next__'))
print(hasattr(g, '__inter__'))
for v in g:
   print(v)

print("-------------------")

def gera2():
    variavel = "Valor 1"
    yield variavel
    variavel = "Valor 2"
    yield variavel
    variavel = "Valor 3"
    yield variavel

g2 = gera2()

print(next(g2))
print(next(g2))
print(next(g2))
print("-------------------")

lista3 = [x for x in range(100)]
print(type(lista3))
print(sys.getsizeof(lista3))

lista4 = (x for x in range(100))
print(type(lista4))
print(sys.getsizeof(lista4))