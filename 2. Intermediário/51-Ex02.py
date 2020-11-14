"""
1 - Crie uma função1 que recebe uma função2 como 
parâmetro e retorne o valor da função2 executada.
"""

def func1():
    return "valor"

def func2(funcao):
    return(funcao)

executar = func2(func1())
print(executar)

"""
2 - Crie uma função1 que recebe uma função2 como 
parâmetro e retorne o valor da função2 executada. 
Faça a função1 executar duas funções que recebam 
um número diferente de argumentos.
"""
def mestre(funcao, *args, **kwargs):
    return funcao(*args, **kwargs)

def oi(nome):
    return f" OI {nome}"

def saudacao(nome,saudacao):
    return f"{saudacao}, {nome}"

executar2 = mestre(oi, "Maria")
print(executar2)