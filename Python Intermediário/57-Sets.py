# SETS(Conjuntos)
#     -Remover elementos duplicados de uma lista
# add(adiciona), update(atualiza), clear, discard(apaga)
# union | (une)
# intersection &  (todos os elementos presentes nos dois sets)
# difference - (elementos apenas do set da esquerda)
# symetric_difference ^ (elementos que estão nos dois sets, mas não em ambos)

#== Criar um set (se não tiver nenhum elemento dentro é dicionario)
s1 = {1,2,3,4,5}
print(f"S1: {s1}")
#== Criar um set vazio
s2 = set()

#==Adicionar elementos
s2.add(1)
s2.add(2)
#s2.add((1,2,3,"Maria"))

s2.update('Python') #recebe um interavel e intera sobre ele
print(f"S2: {s2}")

#== Remover elementos
s2.discard(2)
print(f"S2: {s2}")

#== Não repete elementos iguais
s3 = set()
s3.update([1,2,3,4,5], {5,6,7,8,})
print(f"S3: {s3}")

l2 = ["Luiz", "Joao", "Maria"]
l3 = ["Luiz", "Joao", "Maria", "Luiz", "Luiz","Maria"]

if set(l2) == set(l3):
    print("L2 == L3")
else:
    print("L2 != L3")

#Cast lista => set
l1 = [1,2,1,1,3,4,5,6,6,6,6,6,6,7,8,9,"Leonardo", "Leonardo"]
l1 = set(l1)
l1 = list(l1)
print(f"L1: {l1}")

#== União
s4 = {1,2,3,4,5,7}
s5 = {1,2,3,4,5,6}
s6 = s4 | s5
print(f"S6: {s6}")

#== Intersecção
s7 = s4 & s5
print(f"S7: {s7}")

#== Diferença
s8 = s4 - s5
print(f"S8: {s8}")
s8 = s5 - s4
print(f"S8: {s8}")

#== Elementos em um set especifico, mas não nos dois
s9 = s5 ^ s4
print(f"S9: {s9}")

