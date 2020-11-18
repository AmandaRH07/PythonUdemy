from classes import Cliente, Endereco

cliente1 = Cliente("Eva", 32)
cliente1.insere_endereco("Belo Horizonte", "MG")
print(cliente1.nome)
cliente1.lista_enderecos()
del cliente1
print()
print()


cliente2 = Cliente("Hugo", 55)
cliente2.insere_endereco("Salvador", "BA")
cliente2.insere_endereco("Rio de Janeiro", "RJ")
print(cliente2.nome)
cliente2.lista_enderecos()
print()

cliente3 = Cliente("Pedro", 19)
cliente3.insere_endereco("São Paulo", "SP")
print(cliente3.nome)
cliente3.lista_enderecos()
print()

print("*"*40)

