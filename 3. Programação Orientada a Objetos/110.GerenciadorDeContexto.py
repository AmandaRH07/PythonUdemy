"""Gerenciador de Contexto

Quando esquecemos de fechar algo.
Conecção com base de dados, conexão com rede, arquivos

Ex:
arquivo = open('abc.twt','w')
arquivo.write("Alguma coisa")
arquivo.close()

Assim não precisa do arquivo.close
with open('abc.twt', 'w') as arquivo:
    arquivo.write("Alguma coisa")

"""


# # Forma 1

class Arquivo():
    def __init__(self, arquivo, modo):
        print("abrindo arquivo")
        self.arquivo = open(arquivo, modo)

    def __enter__(self):
        print("retornando arquivo")
        return self.arquivo

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("fechando arquivo")
        self.arquivo.close()
        print(exc_type)
        print(exc_val)
        print(exc_tb)
        # Tratamento de exceção
        return True


with Arquivo('abc.txt', 'w') as arquivo:
    # arquivo.kkkkkkk("Alguma coisa")
    arquivo.write("Alguma coisa")

# Forma 2
from contextlib import contextmanager


@contextmanager
def abrir(arquivo, modo):
    try:
        arquivo = open(arquivo, modo)
        print("Abrindo arquivo")
        # yield faz a função do return sem parar o resto
        yield arquivo
    finally:
        print("fechando arquivo")
        arquivo.close()


with abrir('abc.txt', 'w') as arquivo:
    arquivo.write("Linha 1\n")
    arquivo.write("Linha 2\n")
    arquivo.write("Linha 3\n")
