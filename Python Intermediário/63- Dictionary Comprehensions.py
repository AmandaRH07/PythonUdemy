# Dictionary Comprehensions

lista = [("chave", "valor"), ("chave2", "valor2")]

#d1 = dict(lista)

#== Transformar lista em dicionário, alterando os valores da variavel
d1 = {x : y.upper() for x, y in lista}
print(d1)

#== Set
d2 = {x for x in range(5)}
print(d2, type(d2))


d3 = {f'chave_{x}': x**2 for x in range(5)}
print(d3, type(d3))