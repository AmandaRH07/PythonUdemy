"""
1 - Crie uma função que exibe uma saudação com os parâmetros saudacao e nome.
"""

def saudacao(saudacao, nome):
    print(f"{saudacao} {nome}")

saudacao("Olá","Maria")

"""
2 - Crie uma função que recebe 3 números como parâmetros e exiba a soma entre 
eles.
"""
def soma(n1,n2,n3):
    print(f"{n1} + {n2} + {n3} = {n1+n2+n3}")

n1 = int(input("Número 1: "))
n2 = int(input("Número 2: "))
n3 = int(input("Número 3: "))
soma(n1,n2,n3)

"""
3 - Crie uma função que receba 2 números. O primeiro é um valor e o segundo um
percentual (ex. 10%). Retorne (return) o valor do primeiro número somado
do aumento do percentual do mesmo.
"""

def aumento_Percentual(valor, percentual):
    print(valor + (valor * percentual/100))

valor = int(input("Valor: "))
percentual = int(input("Percentual: "))
aumento_Percentual(valor,percentual)
"""
4 - Fizz Buzz - Se o parâmetro da função for divisível por 3, retorne fizz,
se o parâmetro da função for divisível por 5, retorne buzz. Se o parâmetro da
função for divisível por 5 e por 3, retorne FizzBuzz, caso contrário, retorne o
número enviado.
"""

def FizzBuzz(p):
    if p % 3 == 0 and p % 5 == 0:
        print("FizzBuzz")
    elif p%5 == 0:
        print("Fizz")
    elif p%3 == 0:
        print("Buzz")
    else:
        print(p)

p = int(input("Digite um número: "))
FizzBuzz(p)
