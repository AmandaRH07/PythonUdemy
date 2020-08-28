num_1= 10
num_2= 3
divisao = num_1 /num_2

# print('{:.2f}'.format(divisao))
# print (f'{divisao:.2f}')

n3 = 1

print(f'{n3:0>10}') #completa com 0

n4= 1150

# print(f'{n4:0^10}')
# print(f'{n4:0<10}')

print(f'{n4:0>10.2f}')

nome = 'Amanda'
# print(50-len(nome)/2)
# print(f"{nome:#^50}")
sobrenome = 'hass'
nome_formatado ='{0:$^10} {1:#^10}'.format(nome, sobrenome)
print(nome_formatado)

nome = nome.ljust(10,'#')
print(nome)

nome1= 'Amanda rafaela'
print(nome1.lower()) #tudo minúsculo
print(nome1.upper()) #tudo maiúsculo
print(nome1.title()) #primeiras letras maiusculas
