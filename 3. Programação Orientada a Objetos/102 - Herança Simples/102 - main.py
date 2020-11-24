# Herança = É

from classes import *

c1 = Cliente("Luiz", 45)
c1.falar()
c1.comprar()

a1 = Aluno("Maria", 65)
a1.falar()
a1.estudar()

p1 = Pessoa("João", 43)
p1.falar()

c2 = ClienteVip("Rose", 34, "Silva")
c2.falar()