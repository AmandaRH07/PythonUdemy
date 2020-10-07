#Expressões Lambda - funções anonimas

def funcao(arg, arg2):
    return arg * arg2

var = funcao(2,2)
print(var)

a = lambda x, y: x * y
print(a(2,2))

print("-------------------------") 

lista = [
    ['P1',13],
    ['P2',6],
    ['P3',7],
    ['P4',50],
    ['P5',8],
]

#def func(item):
#    return item[1] # Ordena pelo preço [0,1]
#lista.sort(key= func)

lista.sort(key = lambda item: item[1] )
print(lista)

print("-------------------------") 

# Sem editar a lista original
print(sorted(lista, key = lambda i: i[0], reverse = True))