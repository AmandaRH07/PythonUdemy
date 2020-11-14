from pessoa import Pessoa

#==instancia = cria um objeto a partir de uma classe(molde)
p1 = Pessoa("Ana", 39)
p2 = Pessoa("Paulo", 56)

p1.outro_metodo()

p2.comer("maçã")
p2.parar_comer()
p2.parar_comer()
p2.comer("maçã")

p1.falar("Almoço")
p1.parar_falar()
p2.falar("Café")

print("*"*25)

print(p1.ano_atual)
print(Pessoa.ano_atual)

print(p1.get_ano_nascimento())

#==Objeto