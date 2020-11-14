# Comportamento dos Geradores e Iteradores.py
#== Listas, tuplas, strings -> Sequencias -> Iteraveis

nome = "Ines Regina"

for letra in nome:
    print(letra)

print("-" * 20)

interador = iter(nome)
try:
    print(next(interador)) # I
    print(next(interador)) # n
    print(next(interador))# e
    print(next(interador))# s
    print(next(interador))
    print(next(interador)) # R
    print(next(interador))# e
    print(next(interador))# g
    # print(next(interador))# i
    # print(next(interador)) # n
    # print(next(interador)) # a
except:
    pass

print("CADE OS VALORES?")
for valor in interador:
    print(valor)

print("-" * 20)

gerador = (letra for letra in nome)

print(next(gerador))
print(next(gerador))
print(next(gerador))
print(next(gerador))

print("FOR: ")

for letra in gerador:
    print(letra)

print("outro for: ")

for letra in gerador:
    print(letra)