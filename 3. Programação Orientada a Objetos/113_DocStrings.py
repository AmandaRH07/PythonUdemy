"""DocStrings - Documentação """

variavel = """este módulo não faz nada"""

print(variavel)


def soma(x, y):
    """Soma x e y

    :param x: Primeiro Número
    :type x: int  ou float
    :param y: Segundo Número
    :type y: int  ou float

    :return: Soma de x e y
    :rtype: int ou float

    :raise: os erros que podem acontecer"""
    return x + y


print(soma(1, 3))
help('113_DocStrings')
