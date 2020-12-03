"""
Criando métodos próprios
"""
import  math

pi = math.pi

def dobra_lista(lista):
    return  [x*2 for x in lista]

def multiplica(lista):
    resultado = 1
    for i in lista:
        resultado *= i
    return resultado

# se o método já está sendo importado de
# outro módulo, não executa
if __name__ == '__main__':
    lista = [1,2,3,4,5]
    print(dobra_lista(lista))
    print(pi)
    print(multiplica(lista))
    print(__name__)