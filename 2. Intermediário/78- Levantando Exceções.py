"""
https://docs.python.org/3/library/exceptions.html
criando os próprios tratamentos de exceção
"""

def divide(n1,n2):
    try:
        return n1/n2
    except ZeroDivisionError as error:
        print(error)
        # captura a exceção, faz o log e relança a exceção
        raise

try:
    print(divide(2,0))
except:
    print("erro")

def divide2(n1,n2):
    if n2 == 0:
        raise ValueError("n2 não pode ser 0")
    return n1/n2
try:
    print(divide2(2,0))
except ValueError as error:
    #para o usuario
    print("Você está tentando dividir por 0")
    #para o desenvolvedor
    print('Log:', error)
