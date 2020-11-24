"""
Combinations, permutatios e product
Combinação - Ordem não importa
Permutação - Ordem importa
Ambos não repetem valores únicos
Produto - Ordem importa e repete valores
"""

from itertools import combinations, permutations, product

#Combinations
print("\nCOMBINAÇÃO:")
pessoas = ["Andre", "Eduardo", "Leticia", "Emile", "Fabio", "Helena"]

for grupo in combinations(pessoas,2):
    print(grupo)

# Permutations
print("\nPERMUTAÇÃO:")
pessoas = ["Andre", "Eduardo", "Leticia", "Emile", "Fabio", "Helena"]

for grupo in permutations(pessoas, 2):
    print(grupo)

# Products
print("\nPRODUTO:")
pessoas = ["Andre", "Eduardo", "Leticia", "Emile", "Fabio", "Helena"]

for grupo in product(pessoas, repeat=2):
    print(grupo)
