# List Comprehentions
# Otimização e redução do tamanho do código

l1 = [1,2,3,4,5,6,7,8,9]

#== cada elemento da lista será passado para uma variável
ex1 = [variavel for variavel in l1]
print(ex1)

#== Multiplicar os elementos por 2
ex2 = [v * 2 for v in l1]
print(ex2)

ex3 = [(v, v2) for v in l1 for v2 in range(3)]
print(ex3)

l2 = ["Luiz", "Mauro", "Jorge"]
ex4 = [v.replace("a", "@").upper() for v in l2]

print(ex4)

tupla = (
    ('chave', 'valor'),
    ('chave2', 'valor2'),
)
ex5 = [(x,y) for x,y in tupla]
ex5 = dict(ex5)
print(ex5['chave2'])

l3 = list(range(100))
ex6 = [v for v in l3 if v % 3 == 0 if v % 8 == 0]
print(ex6)

ex7 = [v if v % 3 == 0 and v % 8 == 0  else '*' for v in l3]
print(ex7)
