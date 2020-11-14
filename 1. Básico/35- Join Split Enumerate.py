"""
Split - Dividir string
Join - Juntar uma lista
Enumerate- enumerar elementos
"""

string = "O Brasil é o pais do futebol, o o o o Brasil é penta."

lista_1 = string.split(' ')
lista_2 = string.split(',')

print(lista_1)
print(lista_2)

palavra= ''
contagem = 0
for valor in lista_1:
    qtd_vezes = lista_1.count(valor)
    print(f"A palavra '{valor}' apareceu: {lista_1.count(valor)}x na frase.")

    if (qtd_vezes > contagem):
        contagem = qtd_vezes
        palavra = valor

print(f"A palavra que apareceu mais vezes é '{palavra}' ({contagem}x)")

print ("-----------------------")

string = "O Brasil é penta."
lista = string.split(' ')
string2 = ' '.join(lista)
print(string)
print(lista)
print(string2)

print ("-----------------------")

string = "O Brasil é penta."
lista = string.split(' ')

for indice, valor in enumerate(lista):
    print(indice, valor, " = ", lista[indice])

print ("-----------------------")

listao = [
    [1,"a"],
    [3,"b"],
    [5,"c"],
]
for indice, nome in listao:
    print(indice, nome)