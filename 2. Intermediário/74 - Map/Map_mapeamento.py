"""
Map = mapeamento
Filter = filtrar retorna Verdadeiro ou Falso
Reduce = acumula tudo junto para reduzir depois"""

from Map_dados import *
from functools import reduce

print(lista)

nova_lista = [x * 2 for x in lista]
print(nova_lista)

#map recebe uma função como primeiro argumento
nova_lista2 = map(lambda x: x*2, lista)
print(list(nova_lista2))

for produto in produtos:
    print(produto)

precos = map(lambda p: p["preco"], produtos)
for preco in precos:
    print(preco)

def aumenta_preco(p):
    p['preco'] = round(p['preco'] *1.05, 2)
    return p

novos_produtos = map(aumenta_preco, produtos)
for produto in novos_produtos:
    print(produto)

print("\n\n")

for pessoa in pessoas:
    print(pessoa)

nomes = map(lambda p: p['nome'], pessoas)
for pessoa in nomes:
    print(pessoa)

idades = map(lambda p: p['idade']*1.20, pessoas)
for pessoa in idades:
    print(pessoa)

print("\n\n")

filter_lc = [x for x in lista if x > 5]
print(list(filter_lc))

#filter
lista_fileter = filter(lambda x: x > 5, lista)
print(list(lista_fileter))

nova_lista3 = filter(lambda p: p['preco'] > 50, produtos)
for produto in nova_lista3:
    print(produto)

print("\n\n")

acumula = 0
for item in lista:
    acumula +=item

print(acumula)

#reduce

soma_precos = reduce(lambda ac, item: item + ac, lista, 0 )
print(soma_precos)

