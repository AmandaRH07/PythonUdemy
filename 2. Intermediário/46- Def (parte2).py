def divisao(n1,n2):
    if n2 == 0:
        return 
    return n1/n2
        
divide = divisao(8,0)

if divide:
    print(divide)
else:
    print('Conta inválida')

def f(var):
    print(var)

def dumb():
    return f

var = dumb()
var("Pode imprimir algo na tela")