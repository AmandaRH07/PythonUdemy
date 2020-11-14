def func(*args, **kwargs ):
    print(args)
    print(kwargs['nome'])
    sobrenome = kwargs.get('sobrenome')
    print(sobrenome)
    
lista = [1,2,3,4,5]
print(*lista, 10, 20, sep = '-') #desempacota a tupla e separa por -
func(*lista, nome = "Amanda", sobrenome = "Hass")