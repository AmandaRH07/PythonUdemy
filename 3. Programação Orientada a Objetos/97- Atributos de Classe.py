class Exemplo:
    #variável de classe
    vc = 123

a1 = Exemplo()
a2 = Exemplo()

print(a1.vc)
print(a2.vc)
print(Exemplo.vc)

Exemplo.vc= 321 # para alterar em todas as variáveis
a1.vc = 456
print(a1.__dict__)
print(a2.__dict__)

print(a1.vc)
print(a2.vc)
print(Exemplo.vc)