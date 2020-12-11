"""
Criando Exceções Personalizadas
"""

class MinhaExcecao(Exception):
    pass


def testar():
    raise MinhaExcecao("errado")

try:
    testar()
except MinhaExcecao as error:
    print(f"erro: {error}")