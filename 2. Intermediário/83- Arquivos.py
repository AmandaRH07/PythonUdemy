# Arquivos

#== apagar
import os 

#== para usar o Json
import json

#== Nome do arquivo a ser criado, modo de criação
#-- w+ = leitura e escrita
file = open('abc.txt','w+')

file.write("Linha 1\n")
file.write("Linha 2\n")
file.write("Linha 3\n")

#== mudar o ponteiro do arquivo para um lugar específico
file.seek(0,0)
print("Lendo Linhas: ")
print(file.read())
print("-" * 10)

file.seek(0,0)
print(file.readline(), end = '')
print(file.readline(), end = '')
print(file.readline(), end = '')
print("-" * 10)

file.seek(0,0)
for linha in file.readlines():
    print(linha, end = '')
print("-" * 10)

file.close()

'''
try:
    file = open("abc.txt", 'w+')
    file.write("Linha")
    file.seek(0)
    print(file.read())
finally: 
    file.close()'''

#== Não precisa fechar o arquivo
with open("abc.txt", "w+") as file:
    file.write("Linha 1 \n")
    file.write("Linha 2 \n")
    file.write("Linha 3 \n")

    file.seek(0)
    print(file.read())

#-- r = apenas ler o arquivo
with open("abc.txt", "r") as file:
    print(file.read())

#-- a = adicionar coisas no arquivo, coloca o cursor no fim do arquivo
with open("abc.txt", "a+") as file:
    file.write("Outra linha")
    file.seek(0)
    print(file.read())

#== apagar
os.remove("abc.txt")

#== usar o Json

d1 = {
    'Pessoa1': {
        'nome': 'Joao',
        'idade': 25,
    },
    'Pessoa2': {
        'nome': 'Maria',
        'idade': 27,
    },
}

print(d1)

d1_json = json.dumps(d1, indent=True)
with open("abc.json", 'w+') as file:
    file.write(d1_json)
print(d1_json)
