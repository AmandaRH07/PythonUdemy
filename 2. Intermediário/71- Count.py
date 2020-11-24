"""
count - Intertools
"""

from types import GeneratorType
from itertools import count
variavel = ((x, y) for x, y in zip("alo", "alo"))
print(list(variavel))

print(isinstance(variavel, GeneratorType))

#contador = count(start=5, step=-1)
contador = count(start=5, step= 0.1)
for valor in contador:
    print(round(valor,2))
    # round arredonda com 2 casas decimais

    if valor >= 10:
        break

contador2 = count()
lista = ["a", "B", "c"]
lista = zip(contador2, lista)
print(list(lista))



