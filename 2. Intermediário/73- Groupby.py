"""
Groupby - agrupar
"""

from itertools import groupby, tee

alunos = [
    {"nome": "Luiz", "nota": "A"},
    {"nome": "Joana", "nota": "B"},
    {"nome": "Leticia", "nota": "A"},
    {"nome": "Eduardo", "nota": "C"},
    {"nome": "Andre", "nota": "D"},
    {"nome": "Ana", "nota": "A"},
    {"nome": "Luiza", "nota": "B"},
    {"nome": "José", "nota": "C"},
    {"nome": "Marcia", "nota": "B"},
]

#para não repetir código:
ordena = lambda item: item['nota']

# precisa ordenar as notas
alunos.sort(key=ordena)

for aluno in alunos:
    print(aluno)

print()

alunos_agrupados = groupby(alunos, ordena)

for agrupamento, valores_agrupados in alunos_agrupados:
    va1, va2 = tee(valores_agrupados)

    print(f"Agrupamento: {agrupamento}")
    for aluno in va1:
        print("\t", aluno)

    quantidade =len(list(va2))
    print(f"\t{quantidade} tiraram a nota: {agrupamento}")
    print