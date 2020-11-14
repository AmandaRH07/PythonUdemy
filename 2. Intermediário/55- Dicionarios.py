# no dicionário, o controle das chaves(indices) é feito pelo programador
# par chave - valor

#d1 = {'chave1':'valor'}
d1 = dict(chave1 = "valor da chave", chave2 = "Valor da outra chave")
d1['nova_chave'] = "novo valor"

print(d1)
print(d1['chave1'])
print("------------------")

d2 = {
    "str" : 'valor',
    123 : 'outro valor',
    (1,2,3,4) : 'Tupla',
}

d2['naoexiste'] = 'Agora existe.'
if 'naoexiste' in d2:
    print(      d2[("naoexiste")]    )

print(      d2[(1,2,3,4)]    )
print("------------------")

#Para mudar o conteúdo do valor ligado a chave
d2['str'] = 'assim que muda'
print(d2['str'])

d1.update({'outra_chave': 'novo_valor'})
if d2.get("outra_chave") is not None:
    print(d2.get("outra_chave"))
print("------------------")

d2['nomedachave'] = "Agora ela existe"
if d2.get("nomedachave") is not None:
    print(d2.get("nomedachave"))

print(123)
print("------------------")

# Deletar
print('str' in d2)

del d2['str']
#verifica a chave
print('str' in d2) 

#verifica a chave
print('str' in d2.keys())

#verifica o conteúdo
print('valor' in d2.values()) 
print("------------------")

d3 = {
    'chave1': "valor1",
    'chave2': "valor2",
    'chave3': "valor3",
}

print(len(d3))

# items() acessa a chave e o valor
# values() acessa só o valor e keys() só as chaves
for k in d3.items():
    print(k)
    print(k[0], k[1])

print("------------------")

for k, v in d3.items():
    print(k,v )

print("------------------")

#dicionario dentro de dicionario
clientes = {
    'cliente1' : {
        'nome': 'Luiz',
        'sobrenome' : 'Otavio',
    },
    'cliente2' : {
        'nome': 'Joao',
        'sobrenome' : 'Vitor',
    },
}

for clientes_k, clientes_v in clientes.items():
    print(f"Exibindo {clientes_k}")
    for dados_k,dados_v in clientes_v.items():
        print(f"\t{dados_k} = {dados_v}")

print("------------------")

d4 = {1: 'a', 2: 'b', 3: 'c'}
#copia rasa
v = d4.copy()

print(d4)
print(v)

v[1] = "Marcia"

print(d4)
print(v)

print("------------------")

lista = [
    ['c1', 1],
    ['c2', 2],
    ['c3', 3],
]

d5 = dict(lista)
print(d5)

# apagar elemento
d5.pop('c3')
print(d5)
