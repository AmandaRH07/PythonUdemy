"""
Funções Decoradoras: servem exclusivamente para adicionar
comportamentos em outras funções sem alterar o código delas.
"""
from time import sleep, time

def main(funcao):
    def sub_func(*arg, **kwargs):
        print('agora está decorada')
        funcao()
    #sub_func()
    return sub_func

@main
def fala_oi():
    print("oi")

def outra_funcao(msg):
    print(msg)

fala_oi = main(fala_oi)
fala_oi()

outra_funcao("Eu sou a Maria")
print("#"*20)

def velocidade(funcao):
    def interna(*args,**kwargs):
        start_time = time()
        resultado = funcao(*args,**kwargs)
        end_time = time()
        tempo = (end_time - start_time)*1000
        print(f'A funcao {funcao.__name__} levou {tempo:.2f}ms para executar')
        return resultado
    return interna

def demora():
    for i in range(5):
        print(i)
        sleep(1)

demora()