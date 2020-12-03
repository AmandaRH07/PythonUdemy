"""
O problema dos parâmetros mutáveis em funções
"""

def lista_de_clientes(clientes_iteravel, lista=None):
    if lista is None:
        lista = []
    lista.extend(clientes_iteravel)
    return lista

lista_de_clientes1 = ["Fabio"]
clientes1 = lista_de_clientes(["Joao","Maria", "Eduardo"], lista_de_clientes1)
clientes2 = lista_de_clientes(["Marcos","Jonas", "Felipe"])

print(clientes1)
print(clientes2)