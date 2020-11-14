# Zip --> junta os elementos de listas e exclui o que não dá para juntar 
# Zip_longest --> mostra todos os elementos
#from intertools import zip_longest, count

### Código
cidades = ["São Paulo", "Belo Horizonte", "Salvador", "Monte Belo"]

# Codigo
estados = ["SP", "MG", "BA"]

#cidades_estados = zip(cidades, estados)
cidades_estados = zip(estados,cidades)
#cidades_estados = Zip_longest(estados,cidades)
print(list(cidades_estados))
